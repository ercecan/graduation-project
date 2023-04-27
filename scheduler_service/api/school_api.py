from fastapi import APIRouter
from services.school_db_service import SchoolDBService

school_router = APIRouter(
    prefix="/api/school",
    tags=["School"],
    responses={404: {"description": "Not found"}},
)