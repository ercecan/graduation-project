from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

from enums.grades import Grades
from models.student import Student

from .course import OpenedCourse

V = TypeVar('V') # variable type
D = TypeVar('D') # domain type

# Base class for all constraints
class Constraint(Generic[V, D], ABC):
    def __init__(self, variables: List[V]) -> None:
        self.variables = variables

    @abstractmethod
    def satisfied(self, *args) -> bool:
         ...

class TimeSlotConstraint(Constraint[OpenedCourse, bool]):
    def __init__(self, variables) -> None:
        super().__init__(variables=variables)

    def satisfied(self, assigned_courses: List[OpenedCourse], student: Student) -> bool:
        if len(assigned_courses) == 0 or len(assigned_courses) == 1:
            return True
        
        last_course = list(assigned_courses.keys())[-1]
        courses = list(assigned_courses.keys())[:-1]
        for course in courses:
            for time_slot in course.time_slot:
                for last_time_slot in last_course.time_slot:
                    res = time_slot.is_overlap(last_time_slot)
                    if res:
                        return False
        return True

class PrerequisitiesConstraint(Constraint[OpenedCourse, bool]):
    def __init__(self, variables) -> None:
        super().__init__(variables)

    def satisfied(self, assigned_courses: List[OpenedCourse], student: Student) -> bool:
        if len(assigned_courses) == 0:
            return True
        last_course = list(assigned_courses.keys())[-1]
        if last_course.prereqs == None:
            return True
        
        for prereq in last_course.prereqs:
            for course in student.taken_courses:
                if prereq == course.code and course.grade <= Grades.DD:
                    return True
        return False

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

class MajorConstraint(Constraint[OpenedCourse, bool]):
    def __init__(self, variables) -> None:
        super().__init__(variables=variables)

    def satisfied(self, assigned_courses: List[OpenedCourse], student: Student) -> bool:
        if len(assigned_courses) == 0:
            return True

        last_course = list(assigned_courses.keys())[-1]

        if last_course.major_restrictions == None:
            return True
        
        for major_restriction in last_course.major_restrictions:
            if major_restriction not in [major.code for major in student.major]:
                return False
        return True

class CapacityConstraint(Constraint[OpenedCourse, bool]):
    def __init__(self, variables) -> None:
        super().__init__(variables=variables)

    def satisfied(self, assigned_courses: List[OpenedCourse], student: Student) -> bool:
        if len(assigned_courses) == 0:
            return True
        
        last_course = list(assigned_courses.keys())[-1]
        if last_course.capacity == 0:
            return False
        return True