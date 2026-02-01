from fastapi import APIRouter

films_router = APIRouter(
    prefix="/films",
)

characters_router = APIRouter(
    prefix="/characters",
)

starships_router = APIRouter(
    prefix="/starships",
)

vehicles_router = APIRouter(
    prefix="/vehicles",
)

species_router = APIRouter(
    prefix="/species",
)

planets_router = APIRouter(
    prefix="/planets",
)

from .endpoints import films, characters, starships, vehicles, species, planets