from fastapi import FastAPI
from .api.router import films_router
from .config import lifespan

app = FastAPI(lifespan=lifespan)

# Endpoint raiz
@app.get("/", tags=["Root"])
async def root():
    return {"greetings": "May the Force be with you!"}

app.include_router(films_router)