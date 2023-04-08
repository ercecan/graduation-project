from services.opened_course_db_service import OpenedCourseDBService
from services.student_db_service import StudentDBService
from services.csp_service import CSP
from services.schedule_db_service import ScheduleDBService
from models.preferences import Preference
from models.schedule import Schedule
from typing import List, Any
from dtos.student_dto import StudentSearchDto
from dtos.schedule_dto import ScheduleDto
from service.preference_scorer import PreferenceScorer
from models.time import Term

class SchedulerService:

    def __init__(self, constraints):
        self.student_db_service = StudentDBService()
        self.course_db_service = OpenedCourseDBService()
        self.schedule_db_service = ScheduleDBService()
        self.constraints = constraints
    
    def create_student_dto(self, student_id: str) -> StudentSearchDto:
        student = self.student_db_service.get_student_by_id(student_id)
        taken_courses = self.student_db_service.get_taken_courses(student_id)
        student_dto = StudentSearchDto()
        student_dto.student_id = student.student_id
        student_dto.gpa = student.gpa
        student_dto.major = student.major
        student_dto.year = student.year
        student_dto.remaining_courses = student.remaining_courses
        student_dto.taken_courses = taken_courses
        return student_dto
    
    def create_base_schedules(self, student_dto: StudentSearchDto, term: Term) -> List[Any]:
        remaining_courses = self.student_db_service.get_remaining_courses_ids(student_dto.student_id)
        opened_courses = self.course_db_service.get_opened_courses_by_course_ids(remaining_courses, term)
        
        domains = []
        for variable in opened_courses:
            domains[variable] = [True, False]

        csp_service = CSP(variables=opened_courses, domains=domains)
        for c in self.constraints:
            csp_service.add_constraint(c)
        
        csp_service.backtracking_search(student=student_dto)
        return csp_service.get_all_possible_schedules()


    def score_base_schedules(self, base_schedules: List[Any], preferences: List[Preference]) -> List[Any]:
        preference_scorer = PreferenceScorer(base_schedules)
        for preference in preferences:
            preference_scorer.add_preference(preference)
        
        preference_scorer.scoring()
        return preference_scorer.all_schedules

    def select_best_five_schedules(self, scored_schedules: List[Any]) -> List[Any]:
        scored_schedules.sort(key=lambda x: x[1], reverse=True)
        return scored_schedules[:5]
    
    async def create_schedule_objects(self, student_id: str, base_schedules: List[Any], preferences: List[Preference], term: Term) -> Schedule:
        schedule_dtos = []
        schedules_db = []
        for i, s in enumerate(base_schedules):
            schedule = Schedule()
            schedule.student_id = student_id
            schedule.name = "Schedule " + str(i)
            schedule.preferences = preferences
            schedule.term = term
            schedule.score = s[1]
            schedule.courses = [course.id for course in s[0]]
            schedules_db.append(schedule)

            schedule_dto = ScheduleDto()
            schedule_dto.name = schedule.name
            schedule_dto.score = schedule.score
            schedule_dto.courses = s[0]
            schedule_dto.preferences = preferences
            schedule_dto.student_id = student_id
            schedule_dto.term = term
            schedule_dtos.append(schedule_dto)
        await self.schedule_db_service.save_many_schedules(schedules_db)
        return schedule_dtos
