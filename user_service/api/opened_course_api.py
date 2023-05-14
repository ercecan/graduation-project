from fastapi import APIRouter
from services.opened_course_db_service import OpenedCourseDBService
from services.course_db_service import CourseDBService
from dtos.course_dto import OpenedCourseDto
from utils.opened_course_utils import create_course_from_dto, create_opened_course_from_dto

opened_course_router = APIRouter(
    prefix="/api/opened_course",
    tags=["Opened Course"],
    responses={404: {"description": "Not found"}},
)

opened_course_db_service = OpenedCourseDBService()
course_db_service = CourseDBService()

@opened_course_router.post("/create")
async def create_course(opened_course_dto: OpenedCourseDto):
    try:
        course = await course_db_service.get_course_by_code(opened_course_dto.code)
        if course is None:
            course = create_course_from_dto(opened_course_dto)
            course = await course_db_service.create_course(course)
        opened_course = create_opened_course_from_dto(opened_course_dto, str(course.id))
        opened_course = await opened_course_db_service.create_opened_course(opened_course)
        return opened_course
    except Exception as e:
        print(e)
        raise e