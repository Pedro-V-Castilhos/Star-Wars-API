from app.api.router import starships_router as router
from app.utils import helpers
from fastapi import Request

# Endpoint para solicitar dados de todas as naves espaciais
@router.get("/", tags=["Starships"])
async def get_starships(request: Request, search: str = ""):
    return await helpers.get_from_url(f"https://swapi.dev/api/starships/?search={search}", request)

# Endpoint para solicitar dados de uma nave espacial específica pelo ID
@router.get("/{starship_id}", tags=["Starships"])
async def get_starship(starship_id: int, request: Request):
    return await helpers.get_from_url(f"https://swapi.dev/api/starships/{starship_id}/", request)

# Endpoint para solicitar dados dos filmes de uma nave espacial específica pelo ID
@router.get("/{starship_id}/films", tags=["Films"])
async def get_starship_films(starship_id: int, request: Request):
    responses = await helpers.get_all_from_url(f"https://swapi.dev/api/starships/{starship_id}/","films", request)
    return responses

# Endpoint para solicitar dados dos pilotos de uma nave espacial específica pelo ID
@router.get("/{starship_id}/pilots", tags=["Characters"])
async def get_starship_pilots(starship_id: int, request: Request):
    responses = await helpers.get_all_from_url(f"https://swapi.dev/api/starships/{starship_id}/","pilots", request)
    return responses