from abc import ABC, abstractmethod
from typing import Generic, List, TypeVar

from enums.grades import Grades
from models.course import Course

from dtos.course_dto import OpenedCourseSearchDto
from dtos.student_dto import StudentSearchDto

V = TypeVar('V') # variable type
D = TypeVar('D') # domain type

# Base class for all constraints
class Constraint(Generic[V, D], ABC):

    @abstractmethod
    def satisfied(self, *args) -> bool:
         ...

class TimeSlotConstraint(Constraint[OpenedCourseSearchDto, bool]):

    def satisfied(self, assigned_courses: List[OpenedCourseSearchDto], student: StudentSearchDto) -> bool:
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

class PrerequisitiesConstraint(Constraint[OpenedCourseSearchDto, bool]):

    def satisfied(self, assigned_courses: List[OpenedCourseSearchDto], student: StudentSearchDto) -> bool:
        if len(assigned_courses) == 0:
            return True
        last_course = list(assigned_courses.keys())[-1]
        if last_course.course.prereqs == None:
            return True
        
        for prereq in last_course.course.prereqs:
            for course in student.taken_courses:
                if prereq == course.course.code and course.grade <= Grades.DD:
                    return True
        return False

class YearConstraint(Constraint[OpenedCourseSearchDto, bool]):
    def satisfied(self, assigned_courses: List[OpenedCourseSearchDto], student: StudentSearchDto) -> bool:
        if len(assigned_courses) == 0:
            return True

        years = list(assigned_courses.keys())[-1].course.year_restrictions
        if years == None:
            return True
        return student.year in years

class MajorConstraint(Constraint[OpenedCourseSearchDto, bool]):
    def satisfied(self, assigned_courses: List[OpenedCourseSearchDto], student: StudentSearchDto) -> bool:
        if len(assigned_courses) == 0:
            return True

        last_course = list(assigned_courses.keys())[-1]

        if last_course.course.major_restrictions == None:
            return True
        
        for major_restriction in last_course.course.major_restrictions:
            if major_restriction not in [major.code for major in student.major]:
                return False
        return True

class CapacityConstraint(Constraint[OpenedCourseSearchDto, bool]):

    def satisfied(self, assigned_courses: List[OpenedCourseSearchDto], student: StudentSearchDto) -> bool:
        if len(assigned_courses) == 0:
            return True
        
        last_course = list(assigned_courses.keys())[-1]
        if last_course.course.capacity == 0:
            return False
        return True


class PrerequisitiesFuturePlanConstraint(Constraint[Course, bool]):

    def satisfied(self, assigned_courses: List[Course], student: StudentSearchDto) -> bool:
        if len(assigned_courses) == 0:
            return True
        last_course = list(assigned_courses.keys())[-1]
        if last_course.prereqs == None:
            return True
        
        for prereq in last_course.prereqs:
            for course in student.taken_courses:
                if prereq == course.course.code and course.grade <= Grades.DD:
                    return True
        return False

class YearFuturePlanConstraint(Constraint[Course, bool]):
    def satisfied(self, assigned_courses: List[OpenedCourseSearchDto], student: StudentSearchDto) -> bool:
        if len(assigned_courses) == 0:
            return True

        years = list(assigned_courses.keys())[-1].year_restrictions
        if years == None:
            return True
        return student.year in years

class MajorFuturePlanConstraint(Constraint[Course, bool]):
    def satisfied(self, assigned_courses: List[OpenedCourseSearchDto], student: StudentSearchDto) -> bool:
        if len(assigned_courses) == 0:
            return True

        last_course = list(assigned_courses.keys())[-1]

        if last_course.major_restrictions == None:
            return True
        
        for major_restriction in last_course.major_restrictions:
            if major_restriction not in [major.code for major in student.major]:
                return False
        return True

class MaxCreditFuturePlanConstraint(Constraint[OpenedCourseSearchDto, bool]):
    def satisfied(self, assigned_courses: List[OpenedCourseSearchDto], student: StudentSearchDto) -> bool:
        if len(assigned_courses) == 0:
            return True

        if sum([course.credits for course in assigned_courses]) > 25: #ileride kullanıcıya sor ?
            return False
        return True

class MinCreditFuturePlanConstraint(Constraint[OpenedCourseSearchDto, bool]):
    def satisfied(self, assigned_courses: List[OpenedCourseSearchDto], student: StudentSearchDto) -> bool:
        if len(assigned_courses) == 0:
            return True

        if sum([course.credits for course in assigned_courses]) < 15: #ileride kullanıcıya sor ?
            return False
        return True