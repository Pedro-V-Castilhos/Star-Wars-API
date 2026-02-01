from fastapi import Request
import asyncio

# Helper para operação GET com o cliente de cache HTTP assíncrono
async def get_from_url(url: str, request: Request):
    cache_client = request.app.state.cache_client
    response = await cache_client.get(url)
    return response.json()

async def get_all_from_urls(urls: list[str], request: Request):
    tasks = [get_from_url(url, request) for url in urls]
    responses = await asyncio.gather(*tasks)
    return responses