from fastapi import APIRouter, Response
from service.schedule_service import ScheduleService
from services.redis_service import RedisService
from services.schedule_db_service import ScheduleDBService


schedule_router = APIRouter(
    prefix="/api/schedule",
    tags=["Schedule"],
    responses={404: {"description": "Not found"}},
)

schedule_service = ScheduleService()
schedule_db_service = ScheduleDBService()
r = RedisService()

@schedule_router.post("/")
async def create_schedule(payload: dict):
    try:
        await schedule_service.create_schedule(payload=payload, token='token')
    except Exception as e:
        print(e)
        raise e


@schedule_router.get("/")
async def get_schedule(schedule_id: int):
    '''Given a student id and schedule id, return the schedule for that student'''
    try:
        schedule = schedule_db_service.get_schedule_by_id(schedule_id)
        return schedule
    except Exception as e:
        print(e)
        raise e


# student db id ve term gönderilmeli
@schedule_router.post("/all")
async def get_schedules(payload: dict):
    '''Given a student id, return all schedules for that student'''
    try:
        schedules = await schedule_db_service.get_schedules_by_student_id(payload["student_id"], payload["term"])
        return schedules
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

@schedule_router.delete("/delete/{schedule_id}")
async def delete_schedule(schedule_id: str):
    try:
        await schedule_db_service.delete_schedule(schedule_id)
    except Exception as e:
        print(e)
        raise e
    