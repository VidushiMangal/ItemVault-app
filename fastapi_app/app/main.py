import os
from fastapi import FastAPI
from app.routers import items,auth
from app.database import engine
from app.models import item_model
from app.models import item_db, users_db
from dotenv import load_dotenv

load_dotenv()

item_db.Base.metadata.create_all(bind=engine)
users_db.Base.metadata.create_all(bind=engine)

app=FastAPI()

DEBUG = os.getenv("DEBUG", "false").lower() == "true"
app = FastAPI(debug=DEBUG)

app.include_router(items.router)
app.include_router(auth.router)

@app.get("/healthz")
def health():
    return {"status": "ok"}






