from fastapi import FastAPI
from app.routers import items
from app.database import engine
from app.models import item_model
from app.models import item_db

item_db.Base.metadata.create_all(bind=engine)

app=FastAPI()
app.include_router(items.router)
