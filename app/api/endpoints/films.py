from app.api.router import films_router as router
from app.utils import helpers
from fastapi import Request

# Endpoint para solicitar dados de todos os filmes
@router.get("/")
async def get_films(request: Request):
    return await helpers.get_from_url("https://swapi.dev/api/films/", request)

# Endpoint para solicitar dados de um filme específico pelo ID
@router.get("/{film_id}")
async def get_film(film_id: int, request: Request):
    return await helpers.get_from_url(f"https://swapi.dev/api/films/{film_id}/", request)

# Endpoint para solicitar dados dos personagens de um filme específico pelo ID
@router.get("/{film_id}/characters", tags=["Characters"])
async def get_film_characters(film_id: int, request: Request):
    film_data = await helpers.get_from_url(f"https://swapi.dev/api/films/{film_id}/", request)
    responses = await helpers.get_all_from_urls(film_data["characters"], request)
    return {"results": responses}