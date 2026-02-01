from fastapi import FastAPI
from .api.router import films_router, characters_router, starships_router, vehicles_router, species_router, planets_router
from .config import lifespan

app = FastAPI(lifespan=lifespan)

# Endpoint raiz
@app.get("/", tags=["Root"])
async def root():
    return {"greetings": "May the Force be with you!"}

app.include_router(films_router)
app.include_router(characters_router)
app.include_router(starships_router)
app.include_router(vehicles_router)
app.include_router(species_router)
app.include_router(planets_router)