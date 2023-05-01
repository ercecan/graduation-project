from fastapi import APIRouter, HTTPException, Response
from services.redis_service import RedisService


status_router = APIRouter(
    prefix="/api/status",
    tags=["Status"],
    responses={404: {"description": "Not found"}},
)

r = RedisService()


@status_router.get("/")
async def status_check(id: str, type: str):
    try:
        r_key = f"{type}:{id}"
        status = r.get_val(r_key)
        return Response(status_code=200, content=status)
    except Exception as e:
        print(e)
        raise e
