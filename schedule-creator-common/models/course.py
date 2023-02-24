from beanie import Document, Indexed
from pydantic import BaseModel
from typing import List, Optional
from .time import TimeSlot, Term
from enums.semesters import Semesters
from enums.languages import Languages
from .classroom import Classroom

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
    instructor: Optional[str] = None
    is_elective: Optional[bool] = False

class TakenCourse(Course):
    grade: str
    term: Term

class OpenedCourse(Course, Document):
    time_slot: TimeSlot
    classroom: Optional[Classroom] = None

    class Collection:
        name = "opened_courses"
        Indexes = [
            Indexed(keys=["code"], unique=True),
            Indexed(keys=["crn"], unique=True),
        ]