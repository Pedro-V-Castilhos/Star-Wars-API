from hishel.httpx import AsyncCacheClient
from fastapi import Request

# Helper para operação GET com o cliente de cache HTTP assíncrono
async def get_from_url(url: str, request: Request):
    cache_client = request.app.state.cache_client
    response = await cache_client.get(url)
    return response.json()