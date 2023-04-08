from models.schedule import Schedule
from models.course import FuturePlan
from bson import ObjectId
from typing import List
from dtos.schedule_dto import ScheduleDto
from services.opened_course_db_service import OpenedCourseDBService
class ScheduleDBService:

    def __init__(self):
        self.db = Schedule
        self.course_db_service = OpenedCourseDBService()
    
    async def get_schedule_by_id(self, schedule_id: str) -> ScheduleDto:
        schedule = await self.db.get(ObjectId(schedule_id))
        courses = await self.course_db_service.get_opened_courses_by_course_ids(schedule.courses)

        schedule_dto = ScheduleDto()
        schedule_dto.id = str(schedule.id)
        schedule_dto.name = schedule.name
        schedule_dto.courses = courses
        schedule_dto.term = schedule.term
        schedule_dto.score = schedule.score
        schedule_dto.future_plan = schedule.future_plan
        schedule_dto.preferences = schedule.preferences
        schedule_dto.student_id = schedule.student_id
        return schedule_dto
    
    async def get_schedule_by_name(self, schedule_name: str) -> Schedule:
        schedule =await self.db.find_one(Schedule.name == schedule_name)
        courses = await self.course_db_service.get_opened_courses_by_course_ids(schedule.courses)
        schedule_dto = ScheduleDto()
        schedule_dto.id = str(schedule.id)
        schedule_dto.name = schedule.name
        schedule_dto.courses = courses
        schedule_dto.term = schedule.term
        schedule_dto.score = schedule.score
        schedule_dto.future_plan = schedule.future_plan
        schedule_dto.preferences = schedule.preferences
        schedule_dto.student_id = schedule.student_id
        return schedule_dto
    
    async def get_schedules_by_student_id(self, student_id: str) -> List[ScheduleDto]:
        schedules = await self.db.find(Schedule.student_id == student_id)
        schedules_dto = []
        for schedule in schedules:
            courses = await self.course_db_service.get_opened_courses_by_course_ids(schedule.courses)
            schedule_dto = ScheduleDto()
            schedule_dto.id = str(schedule.id)
            schedule_dto.name = schedule.name
            schedule_dto.courses = courses
            schedule_dto.term = schedule.term
            schedule_dto.score = schedule.score
            schedule_dto.future_plan = schedule.future_plan
            schedule_dto.preferences = schedule.preferences
            schedule_dto.student_id = schedule.student_id
            schedules_dto.append(schedule_dto)
        return schedules_dto
    
    @staticmethod
    async def create_schedule(schedule: Schedule) -> Schedule:
        return await schedule.save()
    
    @staticmethod
    async def update_schedule(schedule: Schedule, schedule_id: str) -> Schedule:
        schedule.id = ObjectId(schedule_id)
        return await schedule.replace()
    
    async def delete_schedule(self, schedule_id: str) -> None:
        schedule = await self.get_schedule_by_id(schedule_id)
        await schedule.delete()

    async def save_many_schedules(self, schedules: List[Schedule]):
        await self.db.insert_many(schedules)
    
    async def add_future_plan(self, schedule_id: str, future_plan: List[FuturePlan]):
        schedule = await self.get_schedule_by_id(schedule_id)
        schedule.future_plan = future_plan
        await schedule.replace()