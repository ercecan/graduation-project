from fastapi import APIRouter, HTTPException, Response
from service.schedule_service import ScheduleService
from services.redis_service import RedisService


schedule_router = APIRouter(
    prefix="/api/schedule",
    tags=["Schedule"],
    responses={404: {"description": "Not found"}},
)

schedule_service = ScheduleService()
r = RedisService()

@schedule_router.post("/")
async def create_schedule(payload: dict):
    try:
        await schedule_service.create_schedule(payload=payload, token='token')
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


@schedule_router.get("/status-check")
async def status_check(id: str):
    try:
        status = r.get_val(key=id)
        return Response(status_code=200, content=status)
    except Exception as e:
        print(e)
        raise e
    