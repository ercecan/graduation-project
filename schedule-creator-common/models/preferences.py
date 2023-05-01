from abc import ABC, abstractmethod
from datetime import datetime
from typing import List
from pydantic import BaseModel

from enums.days import Days

from dtos.course_dto import OpenedCourseSearchDto

class Preference(ABC):
    @abstractmethod
    def __init__(self) -> None:
        ...
    @abstractmethod
    def calculate_score(self, *args) -> bool:
        ...


class DayPreference(Preference):
    def __init__(self, priority, day: Days) -> None:
        super().__init__()
        self.priority = priority
        self.day = day

    def calculate_score(self, assigned_courses: List[OpenedCourseSearchDto]) -> int:
        if len(assigned_courses) == 0:
            return 0
        score = 0
        days = set([time_slot.day for course in assigned_courses for time_slot in course.time_slot])
        if self.day not in days:
            score += self.priority
        return score

class TimePreference(Preference):
    def __init__(self, priority, start_time) -> None:
        super().__init__()
        self.priority = priority
        self.start_time = datetime.strptime(start_time, "%H:%M")

    def calculate_score(self, assigned_courses: List[OpenedCourseSearchDto]) -> int:
        if len(assigned_courses) == 0:
            return 0
        start_times = [datetime.strptime(time_slot.start_time, "%H:%M") for course in assigned_courses for time_slot in course.time_slot]
        for start_time in start_times:
            if self.start_time > start_time:
                return 0
        return self.priority

class InstructorPreference(Preference):
    def __init__(self, priority, instructor) -> None:
        super().__init__()
        self.priority = priority
        self.instructor = instructor

    def calculate_score(self, assigned_courses: List[OpenedCourseSearchDto]) -> int:
        if len(assigned_courses) == 0:
            return 0
        score = 0
        instructors = set([course.instructor for course in assigned_courses])
        if self.instructor not in instructors:
            score += self.priority
        return score