from app.api.router import vehicles_router as router
from app.utils import helpers
from fastapi import Request

# Endpoint para solicitar dados dos veículos baseado em filtros de busca e paginação
# Padrão: Retorna a primeira página sem filtro de busca
@router.get("/")
async def get_vehicles(request: Request, search: str = "", page: str = "", order_by: str = "", reverse: bool = False):
    if page:
        return await helpers.get_from_url(f"https://swapi.dev/api/vehicles/?search={search}&page={page}", request, order_by, reverse)
    return await helpers.get_all_from_pages(f"https://swapi.dev/api/vehicles/?search={search}", request, order_by, reverse)

# Endpoint para solicitar dados de um veículo específico pelo ID
@router.get("/{vehicle_id}")
async def get_vehicle(vehicle_id: int, request: Request):
    return await helpers.get_from_url(f"https://swapi.dev/api/vehicles/{vehicle_id}/", request)

# Endpoint para solicitar dados dos filmes de um veículo específico pelo ID
@router.get("/{vehicle_id}/films")
async def get_vehicle_films(vehicle_id: int, request: Request):
    responses = await helpers.get_all_from_url(f"https://swapi.dev/api/vehicles/{vehicle_id}/","films", request)
    return responses

# Endpoint para solicitar dados dos pilotos de um veículo específico pelo ID
@router.get("/{vehicle_id}/pilots")
async def get_vehicle_pilots(vehicle_id: int, request: Request):
    responses = await helpers.get_all_from_url(f"https://swapi.dev/api/vehicles/{vehicle_id}/","pilots", request)
    return responses
