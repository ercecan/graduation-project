from fastapi import APIRouter
from typing import List
from dtos.schedule_dto import ScheduleDto
from service.scheduler_service import SchedulerService
from services.schedule_db_service import ScheduleDBService
from models.time import Term
from utils.schedule_utils import create_preferences, get_ITU_constraints

schedule_router = APIRouter(
    prefix="/api/schedule",
    tags=["Schedule"],
    responses={404: {"description": "Not found"}},
)

schedule_db_service = ScheduleDBService()
schedule_service = SchedulerService(get_ITU_constraints)

@schedule_router.get("/all")
async def get_all_schedules():
    try:
        return await schedule_db_service.get_schedules_by_student_id()
    except Exception as e:
        print(e)
        raise e

@schedule_router.get("/{schedule_id}")
async def get_schedule_by_id(schedule_id: str):
    try:
        return await schedule_db_service.get_schedule_by_id(schedule_id)
    except Exception as e:
        print(e)
        raise e

@schedule_router.get("/name/{schedule_name}")
async def get_schedule_by_name(schedule_name: str):
    try:
        return await schedule_db_service.get_schedule_by_name(schedule_name)
    except Exception as e:
        print(e)
        raise e

@schedule_router.post("/create")
async def create_schedule(student_id: str, payload: dict):
    try:

        schedule_service = SchedulerService()
        term = Term(year=payload['year'], semester=payload['term'])
        preferences = create_preferences(payload['preferences'])
        student = await schedule_service.create_student_dto(student_id)
        base_schedules = schedule_service.create_base_schedules(student, term)
        scored_schedules = schedule_service.score_base_schedules(base_schedules, preferences=preferences)
        best_schedules = schedule_service.get_best_schedule(scored_schedules)
        response = await schedule_service.create_schedule_objects(student_id=student_id, best_schedules=best_schedules, term=term, preferences=preferences)
        return response
    except Exception as e:
        print(e)
        raise e

@schedule_router.delete("/delete/{schedule_id}")
async def delete_schedule(schedule_id: str):
    try:
        await schedule_db_service.delete_schedule(schedule_id)
    except Exception as e:
        print(e)
        raise e
