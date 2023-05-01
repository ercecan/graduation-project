from fastapi import APIRouter, HTTPException, Response
from service.recommendation_service import RecommendationService
from dtos.schedule_dto import ScheduleDto


recommendation_router = APIRouter(
    prefix="/api/recommendation",
    tags=["Recommendation"],
    responses={404: {"description": "Not found"}},
)

recommendation_service = RecommendationService()



@recommendation_router.post("/")
async def create_recommendation(payload: dict):
    try:
        recommendation_service.create_recommendation(payload=payload, token='token')
    except Exception as e:
        print(e)
        raise e


@recommendation_router.get("/")
async def get_schedule():
    '''Given a student id and recommendation id, return the recommendation for that student'''
    try:
        recommendation_service.get_recommendation()
    except Exception as e:
        print(e)
        raise e


@recommendation_router.get("/all")
async def get_schedules():
    '''Given a student id, return all recommendations for that student'''
    try:
        recommendation_service.get_recommendations()
    except Exception as e:
        print(e)
        raise e