from app.api.router import species_router as router
from app.utils import helpers
from fastapi import Request

# Endpoint para solicitar dados de todas as espécies
@router.get("/")
async def get_species(request: Request, search: str = ""):
    return await helpers.get_from_url(f"https://swapi.dev/api/species/?search={search}", request)

# Endpoint para solicitar dados de uma espécie específica pelo ID
@router.get("/{species_id}")
async def get_species_by_id(species_id: int, request: Request):
    return await helpers.get_from_url(f"https://swapi.dev/api/species/{species_id}/", request)

# Endpoint para solicitar dados dos filmes de uma espécie específica pelo ID
@router.get("/{species_id}/films", tags=["Films"])
async def get_species_films(species_id: int, request: Request):
    responses = await helpers.get_all_from_url(f"https://swapi.dev/api/species/{species_id}/","films", request)
    return responses

# Endpoint para solicitar dados dos personagens de uma espécie específica pelo ID
@router.get("/{species_id}/characters", tags=["Characters"])
async def get_species_people(species_id: int, request: Request):
    responses = await helpers.get_all_from_url(f"https://swapi.dev/api/species/{species_id}/","people", request)
    return responses

# Endpoint para solicitar dados do planeta natal de uma espécie específica pelo ID
@router.get("/{species_id}/homeworld", tags=["Planets"])
async def get_species_homeworld(species_id: int, request: Request):
    species_data = await helpers.get_from_url(f"https://swapi.dev/api/species/{species_id}/", request)
    homeworld_data = await helpers.get_from_url(species_data["homeworld"], request)
    return homeworld_data