from fastapi import FastAPI
from hishel.httpx import AsyncCacheClient

app = FastAPI()

# Endpoint raiz
@app.get("/")
async def root():
    return {"greetings": "May the Force be with you!"}

# Endpoint para solicitar dados de todos os filmes
@app.get("/films")
async def get_films():
    async with AsyncCacheClient() as client:
        response = await client.get("https://swapi.dev/api/films/")
    return response.json()

# Endpoint para solicitar dados de um filme específico pelo ID
@app.get("/films/{film_id}")
async def get_film(film_id: int):
    async with AsyncCacheClient() as client:
        response = await client.get(f"https://swapi.dev/api/films/{film_id}/")
    return response.json()