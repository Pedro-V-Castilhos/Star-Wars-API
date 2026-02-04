from app.api.router import species_router as router
from app.utils import helpers
from fastapi import Request, HTTPException

# Endpoint para solicitar dados das espécies baseado em filtros de busca e paginação
# Padrão: Retorna a primeira página sem filtro de busca
@router.get("/")
async def get_species(request: Request, search: str = "", page: str = "", order_by: str = "", reverse: bool = False):
    helpers.validate_query_params(request, {"search", "page", "order_by", "reverse"})
    helpers.validate_page_parameter(page)
    if page:
        return await helpers.get_from_url(f"https://swapi.dev/api/species/?search={search}&page={page}", request, order_by, reverse)
    return await helpers.get_all_from_pages(f"https://swapi.dev/api/species/?search={search}", request, order_by, reverse)

# Endpoint para solicitar dados de uma espécie específica pelo ID
@router.get("/{species_id}")
async def get_species_by_id(species_id: int, request: Request):
    helpers.validate_query_params(request, set())
    return await helpers.get_from_url(f"https://swapi.dev/api/species/{species_id}/", request)

# Endpoint para solicitar dados dos filmes de uma espécie específica pelo ID
@router.get("/{species_id}/films")
async def get_species_films(species_id: int, request: Request):
    helpers.validate_query_params(request, set())
    responses = await helpers.get_all_from_url(f"https://swapi.dev/api/species/{species_id}/","films", request)
    return responses

# Endpoint para solicitar dados dos personagens de uma espécie específica pelo ID
@router.get("/{species_id}/characters")
async def get_species_people(species_id: int, request: Request):
    helpers.validate_query_params(request, set())
    responses = await helpers.get_all_from_url(f"https://swapi.dev/api/species/{species_id}/","people", request)
    return responses

# Endpoint para solicitar dados do planeta natal de uma espécie específica pelo ID
@router.get("/{species_id}/homeworld")
async def get_species_homeworld(species_id: int, request: Request):
    helpers.validate_query_params(request, set())
    species_data = await helpers.get_from_url(f"https://swapi.dev/api/species/{species_id}/", request)
    homeworld_data = await helpers.get_from_url(species_data["homeworld"], request)
    return homeworld_data