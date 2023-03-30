from typing import List
from enums.grades import Grades
from models.time import Term
from models.course import Course

class TakenCourseDto:
    course: Course
    grade: Grades
    term: Term