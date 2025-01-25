from fastapi import APIRouter
from fastapi.responses import JSONResponse

health_router = APIRouter()


@health_router.get("/", tags=["Health"], response_class=JSONResponse)
async def health():
    """Returns the general health status of the API."""
    return {"health": "OK"}
