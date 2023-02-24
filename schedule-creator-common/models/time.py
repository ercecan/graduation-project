from __future__ import annotations
from pydantic import BaseModel
from enums.days import Days
from enums.semesters import Semesters

class TimeSlot(BaseModel):
    day: Days
    start_time: str
    end_time: str

    @classmethod
    def is_overlap(self, other: TimeSlot) -> bool:
        if self.day != other.day:
            return False
        if self.start_time >= other.end_time or self.end_time <= other.start_time:
            return False
        return True


class Term(BaseModel):
    semester: Semesters
    year: int
    

    
