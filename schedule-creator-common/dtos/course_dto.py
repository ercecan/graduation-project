from enums.grades import Grades
from enums.languages import Languages
from models.time import Term
from models.course import Course
from typing import List, Optional, Any
from enums.teaching_methods import TeachingMethods
from models.classroom import Classroom
from models.time import TimeSlot
from pydantic import BaseModel

class TakenCourseDto:
    id: Optional[str] = None
    course: Course
    grade: Grades
    term: Term

class OpenedCourseDto(BaseModel):
    id: Optional[str] = None
    name: str
    code: str
    crn: str
    ects: int
    credits: int
    language: str = Languages.ENGLISH.value
    major_restrictions: Optional[List[str]] = None
    prereqs: Optional[List[str]] = None
    year_restrictions: Optional[List[int]] = None
    description: Optional[str] = None
    semester: Optional[str] = None
    recommended_semester: Optional[int] = None
    instructor: Optional[str] = None
    is_elective: Optional[bool] = False
    tag: Optional[str] = None
    time: Optional[List[Any]] = None
    classroom: Optional[str] = None
    capacity: Optional[int] = 0
    teaching_method: Optional[str] = None
    term: Any = None

class OpenedCourseSearchDto:
    id: str
    course: Course
    time_slot: List[TimeSlot]
    classroom: Optional[Classroom] = None
    capacity: Optional[int] = 0
    teaching_method: Optional[TeachingMethods] = TeachingMethods.ONSITE

    def __hash__(self) -> int:
        return hash(self.id)