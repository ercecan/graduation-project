import os
from fastapi import APIRouter, HTTPException, Response, File, UploadFile
from models.course import TakenCourse
from enums.semesters import Semesters
from enums.grades import Grades
from models.time import Term

from utils.transcript import extract_courses

transcript_router = APIRouter(
    prefix="/api/transcript",
    tags=["Transcript"],
    responses={404: {"description": "Not found"}},
)


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
            years = term.split()[0]
            semester = term.split()[1]
            year = None
            if semester == "Bahar":
                semester = Semesters.SPRING
                year = int(years.split("-")[1])
            elif semester == "Güz":
                semester = Semesters.FALL
                year = int(years.split("-")[0])
            elif semester == "Yaz":
                semester = Semesters.SUMMER
                year = int(years.split("-")[1])
            term = Term(year=year, semester=semester)
            for course in courses_by_term[term]:
                code = course["code"]
                name = course["name"] 
                letter_grade = course["letter_grade"]
                # get course from code
                # course dict = {code: course_id}
                # course_id = course_dict[code]
                course_id = None
                tc = TakenCourse(course_id=course_id, grade=Grades[letter_grade], term=term)
                taken_courses.append(tc)
                # save taken course into database
                # await taken_course_db_service.create_taken_course(tc)
        # bulk insert taken courses to db 
        # await taken_course_db_service.create_taken_courses(taken_courses)
        
        # delete the file
        os.remove(os.path.abspath(fname))

    # Upload the file to S3
    except Exception as e:
        print(e)
        raise e
