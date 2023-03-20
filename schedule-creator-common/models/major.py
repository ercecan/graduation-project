from typing import List

from pydantic import BaseModel

from .course import Course


class Major(BaseModel):
    name: str
    code: str
    language: str

class MajorPlan(Major):
    courses: List[Course] = None
    total_credits: int = 0