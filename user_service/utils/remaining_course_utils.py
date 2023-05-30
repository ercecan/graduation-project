import pymongo
from bson.objectid import ObjectId
from models.course import TakenCourse
from enums.semesters import Semesters
from enums.grades import Grades
from models.time import Term
import os


m_cli = pymongo.MongoClient(os.getenv("MONGO_URI"))
courses_db = m_cli['schedule-creator']['courses']
tc_db = m_cli['schedule-creator']['taken_courses']
st_db = m_cli['schedule-creator']['students']
sc_db = m_cli['schedule-creator']['schools']


def form_taken_courses(courses_by_term:dict, ):
    taken_courses = []
    for term in courses_by_term:
        year: str = term.split()[0]
        sem: str = term.split()[1]
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

        courses = courses_db.find({"code": {"$in": codes}})
        course_dict = {}
        
        for course in courses:
            course_id = str(course["_id"])
            tc = TakenCourse(course_id=course_id, grade=Grades[code_grade[course['code']]], term=term)
            taken_courses.append(tc)
            course_dict[course["code"]] = str(course["_id"])
    return taken_courses


def get_taken_courses_ids(taken_courses, student_id: str):
    tcs = []
    taken_ids = {}
    for tc in taken_courses:
        taken_ids[tc.course_id] = True
        tc_dict = tc.dict()
        tc_dict['grade'] = tc.grade.value
        tc_dict['term'] = tc.term.dict()
        tc_dict['term']['semester'] = tc.term.semester.value
        tc_dict['term']['year'] = tc.term.year
        tc_dict['student_id'] = student_id
        tcs.append(tc_dict)
    return tcs, taken_ids



def find_remaining_course_ids(student_id: str, taken_ids: dict):
    student = st_db.find_one({"_id": ObjectId(student_id)})
    school_id = student['school_id']
    major_code = student['major'][0]['code']
    school = sc_db.find_one({"_id": ObjectId(school_id)})
    majors = school['majors']
    school_major = list(filter(lambda x: x['code'] == major_code, majors))[0]
    course_ids = school_major['course_ids']
    remaining_course_ids = list(filter(lambda x: not taken_ids.get(x, False), course_ids))
    return remaining_course_ids

