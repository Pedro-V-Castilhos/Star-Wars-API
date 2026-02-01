from app.api.router import vehicles_router as router
from app.utils import helpers
from fastapi import Request

# Endpoint para solicitar dados de todas os veículos
@router.get("/", tags=["Vehicles"])
async def get_vehicles(request: Request, search: str = ""):
    return await helpers.get_from_url(f"https://swapi.dev/api/vehicles/?search={search}", request)

# Endpoint para solicitar dados de um veículo específico pelo ID
@router.get("/{vehicle_id}", tags=["Vehicles"])
async def get_vehicle(vehicle_id: int, request: Request):
    return await helpers.get_from_url(f"https://swapi.dev/api/vehicles/{vehicle_id}/", request)

# Endpoint para solicitar dados dos filmes de um veículo específico pelo ID
@router.get("/{vehicle_id}/films", tags=["Films"])
async def get_vehicle_films(vehicle_id: int, request: Request):
    responses = await helpers.get_all_from_url(f"https://swapi.dev/api/vehicles/{vehicle_id}/","films", request)
    return responses

# Endpoint para solicitar dados dos pilotos de um veículo específico pelo ID
@router.get("/{vehicle_id}/pilots", tags=["Characters"])
async def get_vehicle_pilots(vehicle_id: int, request: Request):
    responses = await helpers.get_all_from_url(f"https://swapi.dev/api/vehicles/{vehicle_id}/","pilots", request)
    return responses
