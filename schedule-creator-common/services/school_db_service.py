from models.school import School
from bson import ObjectId
from services.course_db_service import CourseDBService
from dtos.major_dto import MajorPlanDto

class SchoolDBService:

    def __init__(self):
        self.db = School

    async def get_school_by_id(self, school_id: str) -> School:
        return await self.db.get(ObjectId(school_id))
    
    async def get_school_by_name(self, school_name: str) -> School:
        return await self.db.find_one(School.name == school_name)
    
    @staticmethod
    async def create_school(school: School) -> School:
        return await school.save()
    
    @staticmethod
    async def update_school(school: School, school_id: str) -> School:
        school.id = ObjectId(school_id)
        return await school.replace()
    
    async def delete_school(self, school_id: str) -> None:
        school = await self.get_school_by_id(school_id)
        await school.delete()
    
    async def get_major_plan_by_name(self, school_name: str, major_plan_name: str) -> MajorPlanDto:
        school = await self.get_school_by_name(school_name)
        for major_plan in school.major_plans:
            if major_plan.name == major_plan_name:
                major_plan_dto = MajorPlanDto()
                major_plan_dto.name = major_plan.name
                major_plan_dto.code = major_plan.code
                major_plan_dto.language = major_plan.language
                major_plan_dto.total_credits = major_plan.total_credits
                major_plan_dto.courses = await CourseDBService().get_courses_by_ids(major_plan.course_ids)
                return major_plan_dto
        

