from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.users_db import UserDB
from app.models.users_model import UserCreate
from app.utils.security import hash_password,verify_password, create_access_token
from datetime import timedelta


def create_user_service(db: Session, user: UserCreate):
    existing = db.query(UserDB).filter(UserDB.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    db_user = UserDB(
        email=user.email,
        hashed_password = hash_password(user.password)  # ✅ use helper
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate_user_service(db: Session, email: str, password: str) -> str:
    user = db.query(UserDB).filter(UserDB.email == email).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # Create token with user id or email
    access_token_expires = timedelta(minutes=60)
    access_token = create_access_token(
        data={"sub": str(user.id)},  # subject = user id
        expires_delta=access_token_expires
    )
    return access_token

