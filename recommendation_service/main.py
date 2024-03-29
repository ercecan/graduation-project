from service.consumer_service import Consumer
from services.db_service import DBService
import asyncio
import os

async def init(uri: str):
    await DBService.init_database(uri=uri)
    consumer = Consumer(queue_name='recommendation')
    await consumer.consume()

if __name__ == '__main__':
    uri = os.getenv('MONGO_URI')
    asyncio.run(init(uri=uri))
    print('Consumer started')