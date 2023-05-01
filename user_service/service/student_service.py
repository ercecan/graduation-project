import bcrypt
from models.student import Student
from dtos.student_dto import StudentRegisterDto
from services.student_db_service import StudentDBService
from services.school_db_service import SchoolDBService

class StudentService():

    def __init__(self):
        self.student_db_service = StudentDBService()
        self.school_db_service = SchoolDBService()
        self.gensalt = b'$2b$12$FCkRFDAfluWyd./x1kAPWe'

    async def create_user(self, student_dto: StudentRegisterDto):
        password = self.hash_password(student_dto.password)
        school = await self.school_db_service.get_school_by_name(student_dto.school)
        if school is None:
            raise Exception("School not found")
        print(school)
        student = Student(name=student_dto.name, student_id=student_dto.student_id,  surname=student_dto.surname, email=student_dto.email, password=password, 
                          school_id=str(school.id), major=student_dto.major, year= student_dto.year, gpa=student_dto.gpa,
                          student_type=student_dto.student_type)
        
        
        return await self.student_db_service.create_student(student)

    async def get_user_by_email(self, email: str):
        return await self.student_db_service.get_student_by_email(email)
    
    def verify_password(self, password, hashed_password):
        return self.hash_password(password) == hashed_password
    
    def hash_password(self, password: str) -> str:
        """Returns a salted password hash"""
        return bcrypt.hashpw(password.encode(), self.gensalt).decode()