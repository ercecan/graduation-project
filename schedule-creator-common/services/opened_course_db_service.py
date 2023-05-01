from models.course import OpenedCourse, Course
from bson import ObjectId
from services.course_db_service import CourseDBService
from typing import List
from dtos.course_dto import OpenedCourseSearchDto
from models.time import Term
from beanie.operators import In

class OpenedCourseDBService:

    def __init__(self):
        self.db = OpenedCourse
        self.course_db_service = CourseDBService()
    
    async def get_opened_course_by_id(self, opened_course_id: str) -> OpenedCourse:
        opened_course_db = await self.db.get(ObjectId(opened_course_id))
        course_db = await self.course_db_service.get_course_by_id(opened_course_db.course_id)
        opened_course_db.course = course_db
        return opened_course_db
    
    async def get_opened_course_by_code(self, opened_course_code: str) -> OpenedCourse:
        opened_course_db = await self.db.find_one(OpenedCourse.code == opened_course_code)
        course_db = await self.course_db_service.get_course_by_id(opened_course_db.course_id)
        opened_course_db.course = course_db
        return opened_course_db

    async def get_opened_courses_by_course_ids(self, course_ids: List[str], term: Term) -> List[OpenedCourseSearchDto]:
        opened_course_dtos = []
        opened_courses = await self.db.find(In(OpenedCourse.course_id, course_ids), OpenedCourse.term == term).to_list()
        courses = await self.course_db_service.get_courses_by_ids(course_ids)
        for opened_course in opened_courses:
            for course in courses:
                if str(course.id) == opened_course.course_id:
                    dto = self.create_opened_course_dto(opened_course, course)
                    opened_course_dtos.append(dto)
        return opened_course_dtos

    @staticmethod
    async def create_opened_course(opened_course: OpenedCourse) -> OpenedCourse:
        return await opened_course.save()
    
    @staticmethod
    async def update_opened_course(opened_course: OpenedCourse, opened_course_id: str) -> OpenedCourse:
        opened_course.id = ObjectId(opened_course_id)
        return await opened_course.replace()
    
    async def delete_opened_course(self, opened_course_id: str) -> None:
        opened_course = await self.get_opened_course_by_id(opened_course_id)
        await opened_course.delete()

    @staticmethod
    def create_opened_course_dto(opened_course: OpenedCourse, course: Course) -> OpenedCourseSearchDto:
        dto = OpenedCourseSearchDto()
        dto.id = str(opened_course.id)
        dto.course = course
        dto.time_slot = opened_course.time_slot
        dto.capacity = opened_course.capacity
        dto.classroom = opened_course.classroom
        dto.teaching_method = opened_course.teaching_method
        return dto