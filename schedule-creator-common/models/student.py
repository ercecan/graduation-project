from typing import Any, List, Optional

from beanie import Document, Indexed
from enums.student_types import StudentTypes
from pydantic import BaseModel

from .course import Course, TakenCourse
from .major import Major
from .schedule import Schedule
from .school import School


class Student(BaseModel):
    name: str
    surname: str
    student_id: str
    email: str
    password: str
    gpa: Optional[float] = 0.0
    remaining_courses: Optional[Course] = None
    taken_courses: Optional[List[TakenCourse]] = None # Dictionary olursa, O(1) search
    taken_credits: Optional[int] = 0
    remaining_credits: Optional[int] = 0
    school: Optional[School] = None
    major: List[Major] = None
    schedules: Optional[Schedule] = None
    year: Optional[int] = 0
    student_type: Optional[StudentTypes] = StudentTypes.BACHELOR

    class Collection:
        name = "students"

#isAvailable eklenebilir