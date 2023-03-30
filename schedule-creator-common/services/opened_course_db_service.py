from models.course import OpenedCourse
from bson import ObjectId
from services.course_db_service import CourseDBService

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