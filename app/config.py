from contextlib import asynccontextmanager
from fastapi import FastAPI
from hishel.httpx import AsyncCacheClient

cache_client = None

# Criando um cliente global de cache HTTP assíncrono
@asynccontextmanager
async def lifespan(app: FastAPI):
    global cache_client
    cache_client = AsyncCacheClient()
    try:
        yield
    except Exception:
        print("Um erro ocorreu durante a inicialização do aplicativo:", Exception.__name__)
    finally:
        await cache_client.aclose()