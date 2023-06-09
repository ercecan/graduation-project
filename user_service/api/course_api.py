from typing import List

from dtos.course_dto import AddTakenCourseDTO, UpdateTakenCourseDTO
from fastapi import APIRouter
from models.course import Course
from services.course_db_service import CourseDBService
from services.student_db_service import StudentDBService
from utils.remaining_course_utils import (add_new_taken_course,
                                          delete_remaining_course_by_id,
                                          delete_taken_course_by_id,
                                          update_taken_course_by_id)

course_router = APIRouter(
    prefix="/api/course",
    tags=["Course"],
    responses={404: {"description": "Not found"}},
)

student_db_service = StudentDBService()
course_db_service = CourseDBService()


@course_router.post("/create")
async def create_course(course: Course):
    try:
        course = await course_db_service.create_course(course)
        return course
    except Exception as e:
        print(e)
        raise e

@course_router.post("/all")
async def get_courses_by_ids(ids: List[str]) -> List[Course]:
    try:
        courses = await course_db_service.get_courses_by_ids(ids)
        return courses
    except Exception as e:
        print(e)
        raise e

@course_router.delete('/taken')
async def delete_taken_course(course_id: str, student_id: str):
    try:
        delete_taken_course_by_id(course_id=course_id, student_id=student_id)
    except Exception as e:
        print(e)
        raise e

@course_router.delete('/remaining')
async def delete_remaining_course(course_id: str, student_id: str):
    try:
        delete_remaining_course_by_id(course_id=course_id, student_id=student_id)
    except Exception as e:
        print(e)
        raise e
    
@course_router.get('/remaining')
async def get_remaining_courses(student_id: str):
    try:
        courses = await student_db_service.get_remaining_courses_as_course(student_id=student_id)
        return courses
    except Exception as e:
        print(e)
        raise e
        
@course_router.post('/update/taken')
async def update_taken_course(update_taken_course_dto: UpdateTakenCourseDTO):
    try:
        update_taken_course_by_id(update_taken_course_dto.student_id, update_taken_course_dto.course_id,
                                  update_taken_course_dto.grade, update_taken_course_dto.term.dict())
    except Exception as e:
        print(e)
        raise e
    
@course_router.post('/add/taken')
async def add_taken_course(add_taken_course_dto: AddTakenCourseDTO):
    try:
        course = await course_db_service.get_course_by_id(add_taken_course_dto.course_id)
        if course: 
            add_new_taken_course(add_taken_course_dto.student_id, course.id, add_taken_course_dto.grade, add_taken_course_dto.term)
            delete_remaining_course_by_id(course_id=course.id, student_id=add_taken_course_dto.student_id)
    except Exception as e:
        print(e)
        raise e