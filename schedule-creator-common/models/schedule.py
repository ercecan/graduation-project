from typing import Optional, List

from beanie import Document

from .course import OpenedCourse, FuturePlan
from .time import Term


class Schedule(Document):
    name: str
    courses: Optional[List[OpenedCourse]] = None
    term: Optional[Term] = None
    future_plan: Optional[List[FuturePlan]] = None
    # constraints: Optional[Constraints] = None

    class Collection:
        name = "schedules"
    