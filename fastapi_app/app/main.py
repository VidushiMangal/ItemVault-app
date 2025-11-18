from fastapi import FastAPI
from app.routers import items

app=FastAPI()

@app.get("/")

def root():
    return ("Your Fast API server is running")

app.include_router(items.router)
