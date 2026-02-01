from fastapi import APIRouter

films_router = APIRouter(
    prefix="/films",
    tags=["Films"],
)

characters_router = APIRouter(
    prefix="/characters",
    tags=["Characters"],
)

from .endpoints import films, characters