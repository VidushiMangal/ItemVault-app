from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.item_db import ItemDB
from app.models.item_model import Item

router= APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

items=[]

@router.post("/items")
def create_item(item: Item, db: Session = Depends(get_db)):
    db_item = ItemDB(name=item.name, price=item.price, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/items")
def get_items(db: Session = Depends(get_db)):
    return db.query(ItemDB).all()

@router.get("/items/{item_id}")
def get_item(item_id: int, db: Session = Depends(get_db)):
    return db.query(ItemDB).filter(ItemDB.id == item_id).first()


