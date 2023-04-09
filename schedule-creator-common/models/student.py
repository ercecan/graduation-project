from typing import Any, List, Optional

from beanie import Document, Indexed
from enums.student_types import StudentTypes
from enums.course_tags import Tags

from .course import TakenCourse
from .major import Major


class Student(Document):
    name: str
    surname: str
    student_id: str
    email: str
    password: str
    gpa: Optional[float] = 0.0
    remaining_courses: Optional[List[str]] = None
    taken_courses: Optional[List[TakenCourse]] = None # Dictionary olursa, O(1) search
    taken_credits: Optional[int] = 0
    remaining_credits: Optional[int] = 0
    remaining_tags: Optional[dict] = {tag: 0 for tag in Tags}
    school_id: Optional[str] = None
    major: List[Major] = None
    year: Optional[int] = 0
    student_type: Optional[StudentTypes] = StudentTypes.BACHELOR

    class Settings:
        name = "students"

#isAvailable eklenebilir