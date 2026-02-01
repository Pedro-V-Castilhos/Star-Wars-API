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

species_router = APIRouter(
    prefix="/species",
    tags=["Species"],
)

planets_router = APIRouter(
    prefix="/planets",
    tags=["Planets"],
)

from .endpoints import films, characters, starships, vehicles, species, planets