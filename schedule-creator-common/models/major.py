from typing import Any, List

from pydantic import BaseModel

from .course import Course


class Major(BaseModel):
    name: str
    code: str
    language: str
    # courses: List[Course]