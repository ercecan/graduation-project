import os

import pymongo
from bson.objectid import ObjectId
from enums.grades import Grades
from enums.semesters import Semesters
from fastapi import APIRouter, File, HTTPException, Response, UploadFile
from models.course import TakenCourse
from models.time import Term
from utils.remaining_course_utils import (find_remaining_course_ids,
                                          form_taken_courses,
                                          get_taken_courses_ids)
from utils.transcript import extract_courses

transcript_router = APIRouter(
    prefix="/api/transcript",
    tags=["Transcript"],
    responses={404: {"description": "Not found"}},
)

m_cli = pymongo.MongoClient(os.getenv("MONGO_URI"))
courses_db = m_cli['schedule-creator']['courses']
tc_db = m_cli['schedule-creator']['taken_courses']
st_db = m_cli['schedule-creator']['students']
sc_db = m_cli['schedule-creator']['schools']

@transcript_router.post("/")
async def upload_and_process_transcript(student_id: str, transcript: UploadFile = File(...)):
    try:
        fname = f"{student_id}_transcript.pdf"
        with open(fname, "wb") as buffer:
            buffer.write(transcript.file.read())
        # Read lines from the PDF
        courses_by_term = extract_courses(pdf_path=os.path.abspath(fname))
        # Create taken courses
        taken_courses = form_taken_courses(courses_by_term=courses_by_term)
        # get taken courses ids
        tcs, taken_ids = get_taken_courses_ids(taken_courses=taken_courses, student_id=student_id)
        
        # find remaining courses
        remaining_course_ids = find_remaining_course_ids(student_id=student_id, taken_ids=taken_ids)
        st_db.update_one({'_id': ObjectId(student_id)},{'$set':{'remaining_courses':remaining_course_ids, "taken_courses": tcs}})
        
        # Delete the file
        os.remove(os.path.abspath(fname))

    except Exception as e:
        print(e)
        raise e
