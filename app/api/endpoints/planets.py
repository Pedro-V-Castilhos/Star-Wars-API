from app.api.router import planets_router as router
from app.utils import helpers
from fastapi import Request

# Endpoint para solicitar dados de todos os planetas
@router.get("/")
async def get_planets(request: Request, search: str = ""):
    return await helpers.get_from_url(f"https://swapi.dev/api/planets/?search={search}", request)

# Endpoint para solicitar dados de um planeta específico pelo ID
@router.get("/{planet_id}")
async def get_planet(planet_id: int, request: Request):
    return await helpers.get_from_url(f"https://swapi.dev/api/planets/{planet_id}/", request)

# Endpoint para solicitar dados dos filmes de um planeta específico pelo ID
@router.get("/{planet_id}/films", tags=["Films"])
async def get_planet_films(planet_id: int, request: Request):
    responses = await helpers.get_all_from_url(f"https://swapi.dev/api/planets/{planet_id}/","films", request)
    return responses

# Endpoint para solicitar dados dos residentes de um planeta específico pelo ID
@router.get("/{planet_id}/residents", tags=["Characters"])
async def get_planet_residents(planet_id: int, request: Request):
    responses = await helpers.get_all_from_url(f"https://swapi.dev/api/planets/{planet_id}/","residents", request)
    return responses