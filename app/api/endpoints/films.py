from app.api.router import films_router as router
from app.utils import helpers
from fastapi import Request

# Endpoint para solicitar dados de todos os filmes
@router.get("/")
async def get_films(request: Request, search: str = ""):
    return await helpers.get_from_url(f"https://swapi.dev/api/films/?search={search}", request)

# Endpoint para solicitar dados de um filme específico pelo ID
@router.get("/{film_id}")
async def get_film(film_id: int, request: Request):
    return await helpers.get_from_url(f"https://swapi.dev/api/films/{film_id}/", request)

# Endpoint para solicitar dados dos personagens de um filme específico pelo ID
@router.get("/{film_id}/characters", tags=["Characters"])
async def get_film_characters(film_id: int, request: Request):
    responses = await helpers.get_all_from_url(f"https://swapi.dev/api/films/{film_id}/", "characters", request)
    return {"results": responses}

# Endpoint para solicitar dados dos planetas de um filme específico pelo ID
@router.get("/{film_id}/planets", tags=["Planets"])
async def get_film_planets(film_id: int, request: Request):
    responses = await helpers.get_all_from_url(f"https://swapi.dev/api/films/{film_id}/", "planets", request)
    return {"results": responses}

# Endpoint para solicitar dados das naves espaciais de um filme específico pelo ID
@router.get("/{film_id}/starships", tags=["Starships"])
async def get_film_starships(film_id: int, request: Request):
    responses = await helpers.get_all_from_url(f"https://swapi.dev/api/films/{film_id}/", "starships", request)
    return {"results": responses}

# Endpoint para solicitar dados dos veículos de um filme específico pelo ID
@router.get("/{film_id}/vehicles", tags=["Vehicles"])
async def get_film_vehicles(film_id: int, request: Request):
    responses = await helpers.get_all_from_url(f"https://swapi.dev/api/films/{film_id}/", "vehicles", request)
    return {"results": responses}

# Endpoint para solicitar dados das espécies de um filme específico pelo ID
@router.get("/{film_id}/species", tags=["Species"])
async def get_film_species(film_id: int, request: Request):
    responses = await helpers.get_all_from_url(f"https://swapi.dev/api/films/{film_id}/", "species" , request)
    return {"results": responses}