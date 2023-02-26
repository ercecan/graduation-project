from typing import Optional

from beanie import Document

from .course import Course
from .time import Term


class Schedule(Document):
    name: str
    courses: Optional[Course] = None
    term: Optional[Term] = None
    # constraints: Optional[Constraints] = None

    class Collection:
        name = "schedules"
    