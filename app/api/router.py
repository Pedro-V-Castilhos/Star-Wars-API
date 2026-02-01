from fastapi import APIRouter

films_router = APIRouter(
    prefix="/films",
    tags=["Films"],
)

from .endpoints import films