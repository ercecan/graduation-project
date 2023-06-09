import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from dotenv import load_dotenv
load_dotenv()

from api.student_api import student_router
from api.schedule_api import schedule_router
from api.recommendation_api import recommendation_router
from api.course_api import course_router
from api.school_api import school_router
from api.opened_course_api import opened_course_router
from api.status_api import status_router
from api.transcript_api import transcript_router
from services.db_service import DBService
from services.redis_service import RedisService
from services.publisher_service import Publisher
import pymongo

app = FastAPI()

app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["*"]  # edit later
)


origins = [
    "*",
    "http://localhost:3000",
    "http://localhost:3002",
    "http://localhost:3002/*",
    "http://localhost:3000/*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def start_database():
    mongo_uri = os.getenv('MONGO_URI')
    app.include_router(student_router)
    app.include_router(schedule_router)
    app.include_router(recommendation_router)
    app.include_router(course_router)
    app.include_router(school_router)
    app.include_router(opened_course_router)
    app.include_router(status_router)
    app.include_router(transcript_router)
    await DBService.init_database(uri=mongo_uri)


@app.get("/")
async def root():
    return {"message": "Welcome to Schedule Creator"}

@app.get("/health")
async def health():
    msg = {'status': 'UP'}
    try:
        r = RedisService()
        print(r.host)
        r.set_val('test', 'test')
        print(r.get_val('test'))
        msg['redis'] = 'UP'
    except Exception as e:
        msg['redis'] = 'DOWN'
        msg['redis-error'] = str(e)
    
    try:
        db = pymongo.MongoClient(os.getenv('MONGO_URI'))
        print(db.list_database_names())
        msg['mongodb'] = 'UP'
    except Exception as e:
        msg['mongodb'] = 'DOWN'
        msg['mongodb-error'] = str(e)
    
    try:
        p = Publisher(queue_name='test')
        p.send_message(message='test', token='test')
        msg['rabbitmq'] = 'UP'
    except Exception as e:
        msg['rabbitmq'] = 'DOWN'
        error_msg = e.args[0].exception.strerror
        msg['rabbitmq-error'] = error_msg

    return JSONResponse(content=msg)
