from models.student import Student
from models.course import Course, TakenCourse, FuturePlan
from typing import List
from models.schedule import Schedule
from enums.semesters import Semesters
from dtos.student_dto import StudentSearchDto
from services.csp_service import CSP
from services.course_db_service import CourseDBService
from services.schedule_db_service import ScheduleDBService
from utils.semester_util import next_semester
from utils.constraints_util import get_ITU_constraints
from enums.grades import Grades
from models.time import Term


class RecommendationService:

    def __init__(self, year: int, current_semester: Semesters):
        self.course_db_service = CourseDBService()
        self.schedule_db_service = ScheduleDBService()
        self.constraints = get_ITU_constraints()
        self.year = year
        self.current_semester = current_semester

    def add_schedule_to_student(self, student: StudentSearchDto, schedule: Schedule):
        student.taken_courses = [TakenCourse(course_id=course.id, grade=Grades.CC, term=Term(year=self.year, semester=self.current_semester)) for course in schedule.courses]
        student.remaining_courses = [course.id for course in student.remaining_courses if course not in student.taken_courses]
        return student

    def search(self, schedule_id: str, term_number: int, student: StudentSearchDto) -> List[Course]:
        future_plan = []
        current_semester = self.current_semester
        for i in range(0, term_number):
            semester_next = next_semester(current_semester)
            year = self.year + 1 if semester_next == Semesters.SPRING else self.year
            courses = self.course_db_service.get_courses_by_ids(student.remaining_courses)
            next_semester_courses = [course for course in courses if course.semester == semester_next or course.semester == Semesters.FALL_AND_SPRING or course.semester == Semesters.ALL]

            domains = []
            for variable in next_semester_courses:
                domains[variable] = [True, False]

            csp_service = CSP(variables=next_semester_courses, domains=domains)
            for c in self.constraints:
                csp_service.add_constraint(c)
            
            csp_service.backtracking_search(student=student)
            first_schedule = csp_service.get_all_possible_schedules()[0]
            taken_course_ids = [course.id for course in first_schedule if first_schedule[course] == True]
            taken_courses = [TakenCourse(course_id=course.id, grade=Grades.CC, term=Term(year=year, semester=semester_next)) for course in taken_course_ids]
            student.taken_courses.extend(taken_courses)
            student.remaining_courses = [course for course in student.remaining_courses if course not in taken_course_ids]

            future_plan.append(FuturePlan(term=Term(year=year, semester=semester_next), courses=taken_course_ids))
            current_semester = semester_next
            student.year = student.year + 1 if semester_next == Semesters.SPRING else student.year

        self.schedule_db_service.add_future_plan(schedule_id, future_plan)
        return future_plan