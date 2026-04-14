from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.users_model import UserCreate, UserLogin
from app.services.users_service import create_user_service, authenticate_user_service,list_user_service


router = APIRouter(prefix="/auth", tags=["auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return create_user_service(db, user)

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    token = authenticate_user_service(db, user.email, user.password)
    return {"access_token": token, "token_type": "bearer"}


# COMMENT AS DISPLAYING RECORD EVEN WITH HASHED PASSWORD--SECURITY REASONS
"""@router.get("/getusers")  
def getusers(db: Session = Depends(get_db)):
    return list_user_service(db)"""
