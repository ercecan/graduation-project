from fastapi import APIRouter, HTTPException, Response
from service.schedule_service import ScheduleService
from dtos.schedule_dto import ScheduleDto


schedule_router = APIRouter(
    prefix="/api/schedule",
    tags=["Schedule"],
    responses={404: {"description": "Not found"}},
)

schedule_service = ScheduleService()



@schedule_router.post("/create")
async def create_schedule():
    try:
        schedule_service.create_schedule()
    except Exception as e:
        print(e)
        raise e


@schedule_router.get("/")
async def get_schedule():
    '''Given a student id and schedule id, return the schedule for that student'''
    try:
        schedule_service.get_schedule()
    except Exception as e:
        print(e)
        raise e


@schedule_router.get("/all")
async def get_schedules():
    '''Given a student id, return all schedules for that student'''
    try:
        schedule_service.get_schedules()
    except Exception as e:
        print(e)
        raise e