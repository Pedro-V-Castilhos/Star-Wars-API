from app.api.router import characters_router as router
from app.utils import helpers
from fastapi import Request, HTTPException

# Endpoint para solicitar dados dos personagens baseado em filtros de busca e paginação
# Padrão: Retorna a primeira página sem filtro de busca
@router.get("/")
async def get_characters(request: Request, search: str = "", page: str = "", order_by: str = "", reverse: bool = False):
    helpers.validate_query_params(request, {"search", "page", "order_by", "reverse"})
    helpers.validate_page_parameter(page)
    if page:
        return await helpers.get_from_url(f"https://swapi.dev/api/people/?search={search}&page={page}", request, order_by, reverse)
    return await helpers.get_all_from_pages(f"https://swapi.dev/api/people/?search={search}", request, order_by, reverse)

# Endpoint para solicitar dados de um personagem específico pelo ID
@router.get("/{character_id}")
async def get_character(character_id: int, request: Request):
    helpers.validate_query_params(request, set())
    return await helpers.get_from_url(f"https://swapi.dev/api/people/{character_id}/", request)

# Endpoint para solicitar dados dos filmes de um personagem específico pelo ID
@router.get("/{character_id}/films")
async def get_character_films(character_id: int, request: Request):
    helpers.validate_query_params(request, set())
    responses = await helpers.get_all_from_url(f"https://swapi.dev/api/people/{character_id}/","films", request)
    return responses

# Endpoint para solicitar dados dos veículos de um personagem específico pelo ID
@router.get("/{character_id}/vehicles")
async def get_character_vehicles(character_id: int, request: Request):
    helpers.validate_query_params(request, set())
    responses = await helpers.get_all_from_url(f"https://swapi.dev/api/people/{character_id}/","vehicles", request)
    return responses

# Endpoint para solicitar dados das naves de um personagem específico pelo ID
@router.get("/{character_id}/starships")
async def get_character_starships(character_id: int, request: Request):
    helpers.validate_query_params(request, set())
    responses = await helpers.get_all_from_url(f"https://swapi.dev/api/people/{character_id}/","starships", request)
    return responses

# Endpoint para solicitar dados das espécies de um personagem específico pelo ID
@router.get("/{character_id}/species")
async def get_character_species(character_id: int, request: Request):
    helpers.validate_query_params(request, set())
    responses = await helpers.get_all_from_url(f"https://swapi.dev/api/people/{character_id}/","species", request)
    return responses

# Endpoint para solicitar dados do planeta natal de um personagem específico pelo ID
@router.get("/{character_id}/homeworld")
async def get_character_homeworld(character_id: int, request: Request):
    helpers.validate_query_params(request, set())
    character_data = await helpers.get_from_url(f"https://swapi.dev/api/people/{character_id}/", request)
    homeworld_data = await helpers.get_from_url(character_data["homeworld"], request)
    return homeworld_data