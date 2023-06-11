import uvicorn
from dotenv import load_dotenv
load_dotenv()
from services.db_service import DBService
import asyncio
import os
from service.consumer_service import Consumer


async def init(uri: str):
    await DBService.init_database(uri=uri)
    consumer = Consumer(queue_name='scheduler')
    await consumer.consume()

if __name__ == '__main__':
    uri = os.getenv('MONGO_URI')
    print(f'this is the uri: {uri}')
    asyncio.run(init(uri=uri))
    