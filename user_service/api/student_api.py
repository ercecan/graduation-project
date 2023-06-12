import json

from dtos.student_dto import StudentLoginDto, StudentRegisterDto
from enums.grades import Grades
from fastapi import APIRouter, HTTPException, Response
from models.course import TakenCourse
from models.time import Term
from service.student_service import StudentService
from services.course_db_service import CourseDBService
from services.student_db_service import StudentDBService

student_router = APIRouter(
    prefix="/api/student",
    tags=["Student"],
    responses={404: {"description": "Not found"}},
)

def term_solver(input) : #2018-2019 Bahar Dönemi
    term = input.split()[1]
    years = input.split()[0]
    if term == "Bahar":
        return years.split("-")[1], "spring"
    if term == "Güz":
        return years.split("-")[0], "fall"


student_service = StudentService()
student_db_service = StudentDBService()
course_db_service = CourseDBService()

@student_router.post("/register")
async def register(student_dto: StudentRegisterDto):
    student = await student_service.create_user(student_dto)
    return student


@student_router.post("/login")
async def login_user(student_dto: StudentLoginDto):
    user = await student_service.get_user_by_email(student_dto.email)
    if user:
        if student_service.verify_password(password=student_dto.password, hashed_password=user.password):
            return Response(status_code=200, content=json.dumps({'Message': 'Login Successful', 'email': user.email, 'user_id': str(user.id), 'user_student_id': user.student_id}))
        else:
            raise HTTPException(status_code=401, detail="Incorrect password")
    else:
        raise HTTPException(status_code=404, detail="User not found")

@student_router.post("/remaining")
async def get_remaining_courses(student_id: str):
    courses = await student_db_service.get_remaining_courses_ids(student_id)
    return courses

@student_router.post("/taken")
async def get_taken_courses(student_id: str):
    courses = await student_db_service.get_taken_courses(student_id)
    return courses

@student_router.post("/update")
async def update_user(payload: dict):
    email = payload["email"]
    name = payload["name"] if payload["name"] else ""
    surname = payload["surname"] if payload["surname"] else ""
    student_id = payload["student_id"] if payload["student_id"] else ""
    year = payload["year"] if payload["year"] else ""
    student_db_id = payload["student_db_id"]

    if not email:
        return web.Response(status=422, text="Email is required")

    student = await student_db_service.get_student_by_email(email)
    student.name = name if name else student.name
    student.surname = surname if surname else student.surname
    student.student_id = student_id if student_id else student.student_id
    student.year = year if year else student.year

            
    await student_db_service.update_student(student=student, student_id=student_db_id)
    return student
