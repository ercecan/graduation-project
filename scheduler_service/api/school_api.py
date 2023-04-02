from fastapi import APIRouter

school_router = APIRouter(
    prefix="/api/school",
    tags=["School"],
    responses={404: {"description": "Not found"}},
)