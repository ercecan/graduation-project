import uvicorn
from services.db_service import DBService
import asyncio
from utils.schedule_utils import create_preferences, get_ITU_constraints
from dtos.schedule_dto import ScheduleDto
from service.scheduler_service import SchedulerService
from services.schedule_db_service import ScheduleDBService
from models.time import Term
# from service.consumer_service import Consumer

schedule_service = SchedulerService(get_ITU_constraints())

async def test_create_schedule():
    create_schedule_dto = {"message": "create schedule", "student": "ercecan"
                                , "id": "150180009", "email": "can18@itu.edu.tr", "semester": "spring", "year": 2023, "preferences": [
                                    {"type": "day", "value": "MONDAY", "priority": 5}
                                ], "_id": "641eebfabc338b811292511a"
                                }
    term = Term(year=create_schedule_dto['year'], semester=create_schedule_dto['semester'])
    preferences = create_preferences(create_schedule_dto['preferences'])
    student = await schedule_service.create_student_dto(create_schedule_dto["_id"])
    base_schedules = await schedule_service.create_base_schedules(student, term)
    scored_schedules = await schedule_service.score_base_schedules(base_schedules, preferences=preferences)
    best_schedules = schedule_service.select_best_five_schedules(scored_schedules)
    response = await schedule_service.create_schedule_objects(student_id=create_schedule_dto['_id'], base_schedules=best_schedules, term=term, preferences=create_schedule_dto["preferences"])
    print(response)


async def init():
    await DBService.init_database()
    await test_create_schedule()

if __name__ == '__main__':
    # uvicorn.run('app:app', host="0.0.0.0", port=8003, reload=True)
    asyncio.run(init())
    # consumer = Consumer(queue_name='scheduler')
    # consumer.consume()