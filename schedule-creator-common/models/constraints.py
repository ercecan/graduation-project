from abc import ABC, abstractmethod
from ast import Dict
from typing import Any, Generic, List, Optional, Tuple, TypeVar

from models.student import Student
from pydantic import BaseModel

from .course import OpenedCourse, TakenCourse
from .major import Major

V = TypeVar('V') # variable type
D = TypeVar('D') # domain type
  

# class Constraint(ABC, BaseModel):
#     def __init__(self, weight: int = 1, is_hard: bool = True) -> None:
#         self.weight = weight 
#         self.is_hard = is_hard

#     @abstractmethod
#     def satisfied(self, *args) -> bool:
#         ...
    
#     @abstractmethod
#     def get_cost(self, *args) -> int:
#         ...

# Base class for all constraints
class Constraint(Generic[V, D], ABC):
    # The variables that the constraint is between
    def __init__(self, variables: List[V]) -> None:
        self.variables = variables

    # Must be overridden by subclasses
    @abstractmethod
    def satisfied(self, *args) -> bool:
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

class YearConstraint(Constraint[OpenedCourse, bool]):
    def __init__(self, variables) -> None:
        super().__init__(variables=variables)

    def satisfied(self, assigned_courses: List[OpenedCourse], student: Student) -> bool:
        if len(assigned_courses) == 0:
            return True
        
        years = list(assigned_courses.keys())[-1].year_restrictions
        if years == None:
            return True
        return student.year in years
    def get_cost(self, *args) -> int:
        ...

class MajorConstraint(Constraint[OpenedCourse, bool]):
    def __init__(self, variables) -> None:
        super().__init__(variables=variables)

    def satisfied(self, assigned_courses: List[OpenedCourse], student: Student) -> bool:
        courses = list(assigned_courses.keys())

        for course in courses:
            for major_restriction in course.major_restrictions:
                if major_restriction in [major.code for major in student.major]:
                    return True
        return False

    def get_cost(self, *args) -> int:
        ...