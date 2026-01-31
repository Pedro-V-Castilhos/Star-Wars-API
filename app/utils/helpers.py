from hishel.httpx import AsyncCacheClient

async def get_from_url(url: str):
    async with AsyncCacheClient() as client:
        response = await client.get(url)
    return response.json()