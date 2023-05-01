from fastapi import APIRouter, HTTPException, Response
from dtos.student_dto import StudentLoginDto, StudentRegisterDto
from service.student_service import StudentService
import json


student_router = APIRouter(
    prefix="/api/student",
    tags=["Student"],
    responses={404: {"description": "Not found"}},
)

student_service = StudentService()

@student_router.post("/register")
async def register(student_dto: StudentRegisterDto):
    student = await student_service.create_user(student_dto)
    return student


@student_router.post("/login")
async def login_user(student_dto: StudentLoginDto):
    user = await student_service.get_user_by_email(student_dto.email)
    if user:
        if student_service.verify_password(password=student_dto.password, hashed_password=user.password):
            return Response(status_code=200, content=json.dumps({'Message': 'Login Successful', 'email': user.email, 'user_id': str(user.id)}))
        else:
            raise HTTPException(status_code=401, detail="Incorrect password")
    else:
        raise HTTPException(status_code=404, detail="User not found")
    