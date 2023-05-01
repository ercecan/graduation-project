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

