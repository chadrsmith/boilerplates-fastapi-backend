from fastapi import APIRouter
from .health import get_sys_health

health_router = APIRouter(tags=["Health Check"])

health_router.add_api_route(path="", methods=["GET"], endpoint=get_sys_health)