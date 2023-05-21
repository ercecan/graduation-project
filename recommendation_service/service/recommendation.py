from models.student import Student
from models.course import Course, TakenCourse, FuturePlan
from typing import List
from models.schedule import Schedule
from enums.semesters import Semesters
from dtos.student_dto import StudentSearchDto
from services.csp_service import CSP
from services.course_db_service import CourseDBService
from services.schedule_db_service import ScheduleDBService
from services.student_db_service import StudentDBService
from services.opened_course_db_service import OpenedCourseDBService
from utils.semester_util import next_semester
from enums.grades import Grades
from models.time import Term


class RecommendationService:

    def __init__(self, constraints: list = []):
        self.course_db_service = CourseDBService()
        self.schedule_db_service = ScheduleDBService()
        self.student_db_service = StudentDBService()
        self.opened_course_db_service = OpenedCourseDBService()
        self.constraints = constraints

    async def create_student_dto(self, student_id: str) -> StudentSearchDto:
        student = await self.student_db_service.get_student_by_id(student_id)
        taken_courses = await self.student_db_service.get_taken_courses(student_id)
        student_dto = StudentSearchDto(student_id=student.student_id)
        student_dto.gpa = student.gpa
        student_dto.major = student.major
        student_dto.year = student.year
        student_dto.remaining_courses = student.remaining_courses
        student_dto.taken_courses = taken_courses
        return student_dto

    async def add_schedule_to_student(self, student: StudentSearchDto, schedule_id: str, semester: Semesters, year: int, failed_courses: List[str]) -> StudentSearchDto:
        schedule = await self.schedule_db_service.get_schedule_by_id(schedule_id)
        schedule_courses = schedule.courses
        student.taken_courses = [TakenCourse(course_id=str(course.course.id), grade=Grades.CC, term=Term(year=year, semester=semester))
                                 if course.id not in failed_courses else
                                 TakenCourse(course_id=str(course.course.id), grade=Grades.FF, term=Term(year=year, semester=semester))
                                 for course in schedule_courses]
        remaining_courses = [] 
        for course_id in student.remaining_courses:
            if course_id in [schedule_course.course.id for schedule_course in schedule_courses]:
                if course_id in failed_courses:
                    remaining_courses.append(course_id)
            else:
                remaining_courses.append(course_id)
        student.remaining_courses = remaining_courses
        return student

    async def search(self, schedule_id: str, term_number: int, student: StudentSearchDto, year_: int, current_semester_: Semesters) -> List[Course]:
        future_plan = []
        current_semester = current_semester_
        year = year_
        for i in range(0, term_number):
            semester_next = next_semester(current_semester)
            year = year + 1 if semester_next == Semesters.SPRING.value else year
            courses = await self.course_db_service.get_courses_by_ids(student.remaining_courses)
            next_semester_courses = [course for course in courses if course.semester.value == semester_next or course.semester == Semesters.FALL_AND_SPRING.value or course.semester == Semesters.ALL.value]
            min_semester = min([course.recommended_semester for course in next_semester_courses])
            next_semester_courses = next_semester_courses.filter(lambda course: course.recommended_semester <= min_semester + 2)
            domains = {}
            for variable in next_semester_courses:
                domains[variable] = [True, False]

            csp_service = CSP(variables=next_semester_courses, domains=domains)
            for c in self.constraints:
                csp_service.add_constraint(c)
            
            csp_service.backtracking_search(student=student)
            first_schedule = csp_service.get_all_possible_schedules()[0]
            taken_course_ids = [str(course.id) for course in first_schedule[0]]
            taken_courses = [TakenCourse(course_id=course, grade=Grades.CC, term=Term(year=year, semester=semester_next)) for course in taken_course_ids]
            student.taken_courses.extend(taken_courses)
            student.remaining_courses = [course for course in student.remaining_courses if course not in taken_course_ids]

            future_plan.append(FuturePlan(term=Term(year=year, semester=semester_next), course_ids=taken_course_ids))
            current_semester = semester_next
            student.year = student.year + 1 if semester_next == Semesters.SPRING else student.year

        await self.schedule_db_service.add_future_plan(schedule_id, future_plan)
        return future_plan