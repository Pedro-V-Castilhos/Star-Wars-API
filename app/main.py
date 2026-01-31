from fastapi import FastAPI
from utils import helpers
from config import lifespan

app = FastAPI(lifespan=lifespan)

# Endpoint raiz
@app.get("/")
async def root():
    return {"greetings": "May the Force be with you!"}

# Endpoint para solicitar dados de todos os filmes
@app.get("/films")
async def get_films():
    return await helpers.get_from_url("https://swapi.dev/api/films/")

# Endpoint para solicitar dados de um filme específico pelo ID
@app.get("/films/{film_id}")
async def get_film(film_id: int):
    return await helpers.get_from_url(f"https://swapi.dev/api/films/{film_id}/")