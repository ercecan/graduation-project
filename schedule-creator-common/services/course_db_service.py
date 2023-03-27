from models.course import Course
from bson import ObjectId
from typing import List

class CourseDBService:

    def __init__(self):
        self.db = Course
    
    async def get_course_by_id(self, course_id: str) -> Course:
        return await self.db.get(ObjectId(course_id))
    
    async def get_course_by_code(self, course_code: str) -> Course:
        return await self.db.find_one(Course.code == course_code)
    
    @staticmethod
    async def create_course(course: Course) -> Course:
        return await course.save()
    
    @staticmethod
    async def update_course(course: Course, course_id: str) -> Course:
        course.id = ObjectId(course_id)
        return await course.replace()
    
    async def delete_course(self, course_id: str) -> None:
        course = await self.get_course_by_id(course_id)
        await course.delete()
    
    async def get_courses_by_ids(self, course_ids: List[str]) -> List[Course]:
        ids = [ObjectId(course_id) for course_id in course_ids]
        courses = await self.db.find({"_id": {"$in": ids}}).to_list()
        return courses