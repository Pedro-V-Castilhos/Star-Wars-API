from fastapi import FastAPI, Request
from .utils import helpers
from .config import lifespan

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
    return await helpers.get_from_url(f"https://swapi.dev/api/films/{film_id}/", request    )