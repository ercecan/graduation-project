from typing import List
from fastapi import APIRouter
from models.course import Course
from services.course_db_service import CourseDBService
from utils.remaining_course_utils import delete_taken_course_by_id, delete_remaining_course_by_id, update_taken_course_by_id
from dtos.course_dto import UpdateTakenCourseDTO

course_router = APIRouter(
    prefix="/api/course",
    tags=["Course"],
    responses={404: {"description": "Not found"}},
)

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
async def delete_taken_course(course_id: str, student_id: str):
    try:
        delete_remaining_course_by_id(course_id=course_id, student_id=student_id)
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