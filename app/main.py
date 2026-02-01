from fastapi import FastAPI, Request
from .utils import helpers
from .config import lifespan
import asyncio

app = FastAPI(lifespan=lifespan)

# Endpoint raiz
@app.get("/", tags=["Root"])
async def root():
    return {"greetings": "May the Force be with you!"}

# Endpoint para solicitar dados de todos os filmes
@app.get("/films")
async def get_films(request: Request):
    return await helpers.get_from_url("https://swapi.dev/api/films/", request)

# Endpoint para solicitar dados de um filme específico pelo ID
@app.get("/films/{film_id}")
async def get_film(film_id: int, request: Request):
    return await helpers.get_from_url(f"https://swapi.dev/api/films/{film_id}/", request)

# Endpoint para solicitar dados dos personagens de um filme específico pelo ID
@app.get("/films/{film_id}/characters")
async def get_film_characters(film_id: int, request: Request):
    film_data = await helpers.get_from_url(f"https://swapi.dev/api/films/{film_id}/", request)
    character_urls = film_data.get("characters")
    tasks = [helpers.get_from_url(url, request) for url in character_urls]
    responses = await asyncio.gather(*tasks)
    return {"results": responses}