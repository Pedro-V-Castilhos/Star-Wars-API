from fastapi import FastAPI
from hishel.httpx import AsyncCacheClient

app = FastAPI()

@app.get("/")
async def root():
    return {"greetings": "May the Force be with you!"}