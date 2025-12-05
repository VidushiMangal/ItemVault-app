from fastapi import FastAPI
from app.routers import items,auth
from app.database import engine
from app.models import item_model
from app.models import item_db, users_db

item_db.Base.metadata.create_all(bind=engine)
users_db.Base.metadata.create_all(bind=engine)

app=FastAPI()

app.include_router(items.router)
app.include_router(auth.router)







