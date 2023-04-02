from fastapi import FastAPI
from api.course_api import course_router
from api.opened_course_api import opened_course_router
from api.schedule_api import schedule_router
from services.db_service import DBService


app = FastAPI()

@app.on_event("startup")
async def start_database():
    app.include_router(course_router)
    app.include_router(opened_course_router)
    app.include_router(schedule_router)
    await DBService.init_database()


@app.get("/")
async def root():
    return {"message": "Welcome to Schedule Creator"}

