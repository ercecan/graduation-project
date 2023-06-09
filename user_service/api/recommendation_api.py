from fastapi import APIRouter, HTTPException, Response
from service.recommendation_service import RecommendationService

recommendation_router = APIRouter(
    prefix="/api/recommendation",
    tags=["Recommendation"],
    responses={404: {"description": "Not found"}},
)

recommendation_service = RecommendationService()

@recommendation_router.post("/")
async def create_recommendation(payload: dict):
    try:
        await recommendation_service.create_recommendation(payload=payload, token='token')
    except Exception as e:
        print(e)
        raise e