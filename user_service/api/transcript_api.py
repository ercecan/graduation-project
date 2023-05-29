import os
from fastapi import APIRouter, HTTPException, Response, File, UploadFile
from models.course import TakenCourse
from enums.semesters import Semesters
from enums.grades import Grades
from models.time import Term
import pymongo

from utils.transcript import extract_courses

transcript_router = APIRouter(
    prefix="/api/transcript",
    tags=["Transcript"],
    responses={404: {"description": "Not found"}},
)

m_cli = pymongo.MongoClient(os.getenv("MONGO_URI"))
courses_db = m_cli['schedule-creator']['courses']
tc_db = m_cli['schedule-creator']['taken_courses']


@transcript_router.post("/")
async def upload_and_process_transcript(student_id: str, transcript: UploadFile = File(...)):
    try:
        fname = f"{student_id}_transcript.pdf"
        with open(fname, "wb") as buffer:
            buffer.write(transcript.file.read())
        # Read lines from the PDF
        courses_by_term = extract_courses(pdf_path=os.path.abspath(fname))
        taken_courses = []
        for term in courses_by_term:
            year = term.split()[0]
            sem = term.split()[1]
            semester = Semesters[sem.upper()]
            term = Term(year=year, semester=semester)
            codes = []
            code_grade = {}
            term_hash = f'{term.year} {term.semester.value}'
            for course in courses_by_term[term_hash]:
                code = course["code"]
                name = course["name"] 
                letter_grade = course["letter_grade"]
                if letter_grade == '-':
                    print(f"Course {code} has no grade")
                    continue
                codes.append(code)
                code_grade[code] = letter_grade
                
                course_id = None

            courses = courses_db.find({"code": {"$in": codes}})
            course_dict = {}
            
            for idx, course in enumerate(courses):
                course_id = str(course["_id"])
                

                tc = TakenCourse(course_id=course_id, grade=Grades[code_grade[course['code']]], term=term)
                taken_courses.append(tc)
                course_dict[course["code"]] = str(course["_id"])
        # bulk insert taken courses to db
        tcs = []
        for tc in taken_courses:
            tc_dict = tc.dict()
            tc_dict['grade'] = tc.grade.value
            tc_dict['term'] = tc.term.dict()
            tc_dict['term']['semester'] = tc.term.semester.value
            tc_dict['term']['year'] = tc.term.year
            tc_dict['student_id'] = student_id
            tcs.append(tc_dict)
        tc_db.insert_many(tcs)
        
        # Delete the file
        os.remove(os.path.abspath(fname))

    # Upload the file to S3
    except Exception as e:
        print(e)
        raise e
