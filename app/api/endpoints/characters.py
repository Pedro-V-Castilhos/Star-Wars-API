from app.api.router import characters_router as router
from app.utils import helpers
from fastapi import Request

# Endpoint para solicitar dados de todos os personagens
@router.get("/")
async def get_characters(request: Request, search: str = ""):
    return await helpers.get_from_url(f"https://swapi.dev/api/people/?search={search}", request)

# Endpoint para solicitar dados de um personagem específico pelo ID
@router.get("/{character_id}")
async def get_character(character_id: int, request: Request):
    return await helpers.get_from_url(f"https://swapi.dev/api/people/{character_id}/", request)

# Endpoint para solicitar dados dos filmes de um personagem específico pelo ID
@router.get("/{character_id}/films", tags=["Films"])
async def get_character_films(character_id: int, request: Request):
    responses = await helpers.get_all_from_url(f"https://swapi.dev/api/people/{character_id}/","films", request)
    return responses

# Endpoint para solicitar dados dos veículos de um personagem específico pelo ID
@router.get("/{character_id}/vehicles", tags=["Vehicles"])
async def get_character_vehicles(character_id: int, request: Request):
    responses = await helpers.get_all_from_url(f"https://swapi.dev/api/people/{character_id}/","vehicles", request)
    return responses

# Endpoint para solicitar dados das naves de um personagem específico pelo ID
@router.get("/{character_id}/starships", tags=["Starships"])
async def get_character_starships(character_id: int, request: Request):
    responses = await helpers.get_all_from_url(f"https://swapi.dev/api/people/{character_id}/","starships", request)
    return responses

# Endpoint para solicitar dados das espécies de um personagem específico pelo ID
@router.get("/{character_id}/species", tags=["Species"])
async def get_character_species(character_id: int, request: Request):
    responses = await helpers.get_all_from_url(f"https://swapi.dev/api/people/{character_id}/","species", request)
    return responses

# Endpoint para solicitar dados do planeta natal de um personagem específico pelo ID
@router.get("/{character_id}/homeworld", tags=["Planets"])
async def get_character_homeworld(character_id: int, request: Request):
    character_data = await helpers.get_from_url(f"https://swapi.dev/api/people/{character_id}/", request)
    homeworld_data = await helpers.get_from_url(character_data["homeworld"], request)
    return homeworld_data