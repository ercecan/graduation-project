import os
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from models.student import Student
from models.course import Course, OpenedCourse
from models.school import School
from models.schedule import Schedule
from enums.languages import Languages
from models.major import Major
from dotenv import load_dotenv

load_dotenv()

class DBService:
    @staticmethod
    async def init_database():
        try:
            client = AsyncIOMotorClient("mongodb://localhost:27017")
            await init_beanie(
                database=client["schedule-creator"],
                document_models=[Student, Course, OpenedCourse, School, Schedule],
            )
        except Exception as e:
            print(e)