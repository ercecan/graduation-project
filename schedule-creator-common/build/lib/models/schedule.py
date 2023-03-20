from typing import Optional, List

from pydantic import BaseModel

from .course import OpenedCourse, FuturePlan
from .time import Term


class Schedule(BaseModel):
    name: str
    courses: Optional[List[OpenedCourse]] = None
    term: Optional[Term] = None
    future_plan: Optional[List[FuturePlan]] = None
    # constraints: Optional[Constraints] = None

    class Collection:
        name = "schedules"
    