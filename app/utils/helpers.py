from hishel.httpx import AsyncCacheClient
from app.config import cache_client

# Helper para operação GET com o cliente de cache HTTP assíncrono
async def get_from_url(url: str):
    response = await cache_client.get(url)
    return response.json()