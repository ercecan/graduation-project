import os

import pymongo
from bson.objectid import ObjectId
from enums.grades import Grades
from enums.semesters import Semesters
from models.course import TakenCourse
from models.time import Term

m_cli = pymongo.MongoClient(os.getenv("MONGO_URI"))
courses_db = m_cli['schedule-creator']['courses']
tc_db = m_cli['schedule-creator']['taken_courses']
st_db = m_cli['schedule-creator']['students']
sc_db = m_cli['schedule-creator']['schools']


def form_taken_courses(courses_by_term:dict, ):
    taken_courses = []
    all_codes = []
    code_grade = {}
    for term in courses_by_term:
        year: str = term.split()[0]
        sem: str = term.split()[1]
        semester = Semesters[sem.upper()]
        term = Term(year=year, semester=semester)
        codes = []
        
        
        term_hash = f'{term.year} {term.semester.value}'
        for course in courses_by_term[term_hash]:
            
            code = course["code"]
            if code == 'ATA 101':
                code = 'ATA 121'
            elif code == 'ATA 102':
                code = 'ATA 122'
            elif code == 'TUR 102':
                code = 'TUR 122' 
            elif code == 'ING 112':
                code = 'ING 112A' 
            elif code == 'TUR 101':
                code = 'TUR 121' 
            elif code == 'ING 201':
                code = 'ING 201A' 
            elif code == 'MAT 210E':
                code = 'BLG 210E' 
            elif code == 'DAN 101':
                code = 'DAN 102'
            elif code == 'DAN 301':
                continue
            
            name = course["name"] 
            letter_grade = course["letter_grade"]
            if letter_grade == '-':
                print(f"Course {code} has no grade")
                continue
            codes.append(code)
            
            code_grade[code] = letter_grade
            all_codes.append(code)
        if 'ING 100' not in all_codes:
            all_codes.append('ING 100')
            code_grade['ING 100'] = 'AA'
            codes.append('ING 100')
        courses = list(courses_db.find({"code": {"$in": codes}}))
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


def delete_taken_course_by_id(course_id: str, student_id: str):
    try:
        # remove from taken_courses
        st_db.update_one({"_id": ObjectId(student_id)}, {"$pull": {"taken_courses": {"course_id": course_id}}})
        # add to remaining_courses
        st_db.update_one({"_id": ObjectId(student_id)}, {"$push": {"remaining_courses": course_id}})
        return True
    
    except Exception as e:
        print(e)
        raise e


def delete_remaining_course_by_id(course_id: str, student_id: str):
    try:
        st_db.update_one({"_id": ObjectId(student_id)}, {"$pull": {"remaining_courses": str(course_id)}})
        return True
    except Exception as e:
        print(e)
        raise e
    
def add_new_taken_course(student_id: str, course_id: str, grade: Grades, term: Term):
    try:
        taken_course = {
            "course_id": str(course_id),
            "grade": grade.value,
            "term": {
                "semester": term.semester.value,
                "year": term.year
            }
        }

        arr = st_db.update_one(
            {"_id": ObjectId(student_id)},
            {"$push": {"taken_courses": taken_course}}
        )
        return
    except Exception as e:
        print(e)
        raise e

def update_taken_course_by_id( student_id: str, course_id: str, grade: str, term):
    try:
        print(term['semester'].value, term['year'])
        
        st_db.update_one({"_id": ObjectId(student_id), "taken_courses.course_id": course_id}, 
                         {"$set": 
                          {"taken_courses.$.grade": grade.value, 
                           "taken_courses.$.term.semester": term['semester'].value, 
                           "taken_courses.$.term.year": term['year']}})
        return True
    except Exception as e:
        print(e)
        raise e