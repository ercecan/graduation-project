import uvicorn
from dotenv import load_dotenv
load_dotenv()
from services.db_service import DBService
import asyncio
from utils.schedule_utils import create_preferences, get_ITU_constraints
from dtos.schedule_dto import ScheduleDto
from service.scheduler_service import SchedulerService
from services.schedule_db_service import ScheduleDBService
from models.time import Term
import os
from service.consumer_service import Consumer

# from service.consumer_service import Consumer

async def init(uri: str):
    await DBService.init_database(uri=uri)
    consumer = Consumer(queue_name='scheduler')
    await consumer.consume()

if __name__ == '__main__':
    # uvicorn.run('app:app', host="0.0.0.0", port=8003, reload=True)
    uri = os.getenv('MONGO_URI')
    asyncio.run(init(uri=uri))
    