from typing import List, Optional, Tuple, Any
from abc import ABC, abstractmethod
from pydantic import BaseModel
from .course import OpenedCourse, TakenCourse
from .major import Major

class Constraint(ABC, BaseModel):
    def __init__(self, weight: int = 1, is_hard: bool = True) -> None:
        self.weight = weight 
        self.is_hard = is_hard

    @abstractmethod
    def satisfied(self, *args) -> bool:
        ...
    
    @abstractmethod
    def get_cost(self, *args) -> int:
        ...

class TimeSlotConstraint(Constraint):
    def __init__(self, weight: int = 100, is_hard: bool = True) -> None:
        super().__init__(weight, is_hard)

    def satisfied(self, new_course: OpenedCourse, assigneds: List[OpenedCourse]) -> bool:
        for assigned in assigneds:
            if assigned.time_slot.is_overlap(new_course.time_slot):
                return False
        return True

    def get_cost(self, *args) -> int:
        ...

class MajorConstraint(Constraint):
    def __init__(self, weight: int = 100, is_hard: bool = True) -> None:
        super().__init__(weight, is_hard)

    def satisfied(self, new_course: OpenedCourse, student_major: Major) -> bool:
        return student_major in new_course.major_restrictions
    

    def get_cost(self, *args) -> int:
        ...

class PrereqConstraint(Constraint):
    def __init__(self, weight: int = 100, is_hard: bool = True) -> None:
        super().__init__(weight, is_hard)

    def satisfied(self, new_course: OpenedCourse, taken_courses: List[TakenCourse]) -> bool:
        if new_course.prereqs == None:
            return True
        
        for prereq in new_course.prereqs:
            for taken_course in taken_courses:
                if prereq == taken_course.code and taken_course.grade <= "DD":
                    return True
        return False

    def get_cost(self, *args) -> int:
        ...

class YearConstraint(Constraint):
    def __init__(self, weight: int = 100, is_hard: bool = True) -> None:
        super().__init__(weight, is_hard)

    def satisfied(self, new_course: OpenedCourse, student_year: int) -> bool:
        if new_course.year_restrictions == None:
            return True
        return student_year in new_course.year_restrictions

    def get_cost(self, *args) -> int:
        ...

