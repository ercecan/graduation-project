from typing import Optional, Any, List
from beanie import Document, Indexed
from major import Major
from course import TakenCourse, Course
from school import School
from schedule import Schedule
from enums.student_types import StudentTypes

class Student(Document):
    name: str
    surname: str
    student_id: str
    email: str
    password: str
    gpa: Optional[float] = 0.0
    remaining_courses: Optional[Course] = None
    taken_courses: Optional[TakenCourse] = None
    taken_credits: Optional[int] = 0
    remaining_credits: Optional[int] = 0
    school: Optional[School] = None
    major: List[Major] = None
    schedules: Optional[Schedule] = None
    year: Optional[int] = 0
    student_type: Optional[StudentTypes] = StudentTypes.BACHELOR

    class Collection:
        name = "students"
        Indexes = [
            Indexed(keys=["email"], unique=True),
        ]