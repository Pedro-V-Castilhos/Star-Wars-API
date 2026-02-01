from fastapi import APIRouter

films_router = APIRouter(
    prefix="/films",
    tags=["Films"],
)

characters_router = APIRouter(
    prefix="/characters",
    tags=["Characters"],
)

starships_router = APIRouter(
    prefix="/starships",
    tags=["Starships"],
)

vehicles_router = APIRouter(
    prefix="/vehicles",
    tags=["Vehicles"],
)

from .endpoints import films, characters, starships, vehicles