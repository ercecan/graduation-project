from models.student import Student
from models.course import Course
from typing import List
from models.schedule import Schedule


class Recommendation:
    def __init__(self, student: Student, schedules: List[Schedule]) -> None:
        self.student = student
        self.schedules = schedules


    def search(self) -> List[Course]:
        ...
