from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.item_db import ItemDB # Database Model
from app.models.item_model import Item # Pydantic Model

router= APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

items=[]
#Adding A Record
@router.post("/items")
def create_item(item: Item, db: Session = Depends(get_db)):
    db_item = ItemDB(name=item.name, price=item.price, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    print("One Record Added")
    return db_item

#Listing All Records
@router.get("/items")
def get_items(db: Session = Depends(get_db)):
    print("Listing All Records")
    return db.query(ItemDB).all()

#Retrieving A Record with Given ID
@router.get("/items/{item_id}")
def get_item(item_id: int, db: Session = Depends(get_db)):
    return db.query(ItemDB).filter(ItemDB.id == item_id).first()

#Updating A Record with Given ID    
@router.put("/items/{item_id}")
def update_item(item_id: int, item: Item, db: Session = Depends(get_db)):
    db_item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.name = item.name
    db_item.price = item.price
    db_item.description = item.description
    db.commit()
    db.refresh(db_item)
    print("Item Updated")
    return db_item

#Deleting A Record with Given ID
@router.delete("/items/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"Item deleted"}

#Listing Record by specifying limit(how many) and skip ( how many to skip from beginning)
@router.get("/items_paginated")
def get_items_paginated(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = db.query(ItemDB).offset(skip).limit(limit).all()
    return items
