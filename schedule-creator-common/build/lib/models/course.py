from typing import List, Optional

from beanie import Document, Indexed
from enums.grades import Grades
from enums.languages import Languages
from enums.semesters import Semesters
from enums.teaching_methods import TeachingMethods
from enums.course_tags import Tags
from pydantic import BaseModel

from .classroom import Classroom
from .time import Term, TimeSlot


class Course(BaseModel):
    name: str
    code: str
    crn: str
    ects: int
    credits: int
    language: Languages = Languages.ENGLISH
    major_restrictions: Optional[List[str]] = None
    prereqs: Optional[List[str]] = None
    year_restrictions: Optional[List[int]] = None
    description: Optional[str] = None
    semester: Optional[Semesters] = None
    recommended_semester: Optional[int] = None
    instructor: Optional[str] = None
    is_elective: Optional[bool] = False
    tag: Optional[Tags] = None
    

class TakenCourse(BaseModel):
    course: Course
    grade: Grades
    term: Term

class OpenedCourse(BaseModel):
    course: Course
    time_slot: List[TimeSlot]
    classroom: Optional[Classroom] = None
    capacity: Optional[int] = 0
    teaching_method: Optional[TeachingMethods] = TeachingMethods.ONSITE
    

    class Collection:
        name = "opened_courses"
    
    def __hash__(self):
        return 3*self.ects**3 + 2*self.ects**2 - 5
    
class FuturePlan(BaseModel):
    course: Course
    term: Term