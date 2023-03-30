from models import Student
from bson import ObjectId
from typing import List
from dtos.course_dto import TakenCourseDto
from services.course_db_service import CourseDBService

class StudentDBService:

    def __init__(self):
        self.db = Student

    async def get_student_by_student_id(self, student_id: str) -> Student:
        return await self.db.find_one(Student.student_id == student_id)

    async def get_student_by_email(self, student_email: str) -> Student:
        return await Student.find_one(Student.email == student_email)

    async def get_student_by_username(self, student_username: str) -> Student:
        return await self.db.find_one(Student.username == student_username)

    async def get_student_by_id(self, student_id: str) -> Student:
        return await self.db.get(ObjectId(student_id))

    @staticmethod
    async def create_student(student: Student) -> Student:
        return await student.save()
    
    @staticmethod
    async def update_student(student: Student, student_id: str) -> Student:
        student.id = ObjectId(student_id)
        return await student.replace()
    
    async def delete_student(self, student_id: str) -> None:
        student = await self.get_student_by_id(student_id)
        await student.delete()
    
    async def get_taken_courses(self, student_id: str) -> List[TakenCourseDto]:
        student = await self.get_student_by_id(student_id)
        ids = [ObjectId(course_id) for course_id in student.taken_courses]
        taken_courses = CourseDBService().get_courses_by_ids(ids)
        return taken_courses