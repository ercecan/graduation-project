from fastapi import APIRouter
from models.school import School
from services.school_db_service import SchoolDBService

school_router = APIRouter(
    prefix="/api/school",
    tags=["School"],
    responses={404: {"description": "Not found"}},
)

school_service = SchoolDBService()

@school_router.post("/create")
async def create(school_dto: School):
    student = await school_service.create_school(school_dto)
    return student

@school_router.get("/courses/all")
async def get_all_courses_of_major(school_id: str, major_plan_name: str):
    try:
        course_ids = await school_service.get_all_course_ids(school_id=school_id, major_plan_name=major_plan_name)
        return course_ids
    except Exception as e:
        print(e)
        raise e