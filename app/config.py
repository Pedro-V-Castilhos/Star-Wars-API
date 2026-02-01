from contextlib import asynccontextmanager
from fastapi import FastAPI
from hishel.httpx import AsyncCacheClient

# Criando um cliente global de cache HTTP assíncrono
@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.cache_client = AsyncCacheClient()
    yield
    await app.state.cache_client.aclose()