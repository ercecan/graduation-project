from typing import List
from dtos.course_dto import OpenedCourseSearchDto

class ScheduleDto:
    name: str
    courses: List[OpenedCourseSearchDto] = None
    term: str = None
    score: int = None
    future_plan: List[str] = None
    preferences: List[str] = None
    student_id: str = None