from fastapi import APIRouter

### Import Routers ###
from .health import health_router

### Create Router for API ###
api_router = APIRouter()

### Register Routes ###
api_router.include_router(health_router, prefix='/health', include_in_schema=False)
