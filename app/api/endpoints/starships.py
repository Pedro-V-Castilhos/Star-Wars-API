from app.api.router import starships_router as router
from app.utils import helpers
from fastapi import Request

# Endpoint para solicitar dados das naves espaciais baseado em filtros de busca e paginação
# Padrão: Retorna a primeira página sem filtro de busca
@router.get("/")
async def get_starships(request: Request, search: str = "", page: str = "", order_by: str = "", reverse: bool = False):
    if page:
        return await helpers.get_from_url(f"https://swapi.dev/api/starships/?search={search}&page={page}", request, order_by, reverse)
    return await helpers.get_all_from_pages(f"https://swapi.dev/api/starships/?search={search}", request, order_by, reverse)

# Endpoint para solicitar dados de uma nave espacial específica pelo ID
@router.get("/{starship_id}")
async def get_starship(starship_id: int, request: Request):
    return await helpers.get_from_url(f"https://swapi.dev/api/starships/{starship_id}/", request)

# Endpoint para solicitar dados dos filmes de uma nave espacial específica pelo ID
@router.get("/{starship_id}/films")
async def get_starship_films(starship_id: int, request: Request):
    responses = await helpers.get_all_from_url(f"https://swapi.dev/api/starships/{starship_id}/","films", request)
    return responses

# Endpoint para solicitar dados dos pilotos de uma nave espacial específica pelo ID
@router.get("/{starship_id}/pilots")
async def get_starship_pilots(starship_id: int, request: Request):
    responses = await helpers.get_all_from_url(f"https://swapi.dev/api/starships/{starship_id}/","pilots", request)
    return responses