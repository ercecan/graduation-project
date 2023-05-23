from typing import List
from fastapi import APIRouter
from models.course import Course
from services.course_db_service import CourseDBService

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