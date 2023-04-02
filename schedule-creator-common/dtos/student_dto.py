from typing import List, Optional
from enums.languages import Languages
from enums.student_types import StudentTypes
from models.course import Course, TakenCourse
from models.major import Major

class StudentDto:
    name: str
    surname: str
    student_id: str
    email: str
    password: str
    gpa: Optional[float] = 0.0
    taken_courses: Optional[dict] = None
    taken_credits: Optional[int] = 0
    school: Optional[str] = None
    major: List[str] = None
    year: Optional[int] = 0
    student_type: str = StudentTypes.BACHELOR.value
    
class StudentSearchDto:
    student_id: str
    gpa: Optional[float] = 0.0
    taken_courses: Optional[List[TakenCourse]] = None
    remaining_courses: Optional[List[str]] = None
    major: List[Major] = None
    year: Optional[int] = 0
