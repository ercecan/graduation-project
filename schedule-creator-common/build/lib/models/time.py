from __future__ import annotations

from datetime import datetime

from enums.days import Days
from enums.semesters import Semesters
from pydantic import BaseModel


class TimeSlot(BaseModel):
    day: Days
    start_time: str
    end_time: str

    def is_overlap(self, other: TimeSlot) -> bool:
        if self.day != other.day:
            return False
        self_start_time = datetime.strptime(self.start_time, "%H:%M")
        self_end_time = datetime.strptime(self.end_time, "%H:%M")
        other_start_time = datetime.strptime(other.start_time, "%H:%M")
        other_end_time = datetime.strptime(other.end_time, "%H:%M")
        if self_start_time >= other_end_time or self_end_time <= other_start_time:
            return False
        return True

class Term(BaseModel):
    semester: Semesters
    year: int
    

    
