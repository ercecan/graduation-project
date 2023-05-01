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
from api.status_api import status_router
from services.db_service import DBService


app = FastAPI()

app.add_middleware(
    TrustedHostMiddleware, allowed_hosts=["*"]  # edit later
)


origins = [
    "*",
    "http://localhost:3000",
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
    app.include_router(status_router)
    await DBService.init_database(uri=mongo_uri)