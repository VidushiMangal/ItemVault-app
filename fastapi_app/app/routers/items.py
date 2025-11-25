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
def get_item_all(db: Session = Depends(get_db)):
    print("Listing All Records")
    return db.query(ItemDB).all()

#Retrieving A Record with Given ID
@router.get("/items/{item_id}")
def get_item_by_id(item_id: int, db: Session = Depends(get_db)):
    return db.query(ItemDB).filter(ItemDB.id == item_id).first()

# Filtering on the basis of type(example name=Laptop)
@router.get("/items/name/{item_name}")
def get_item_by_name(item_name:str, db: Session = Depends(get_db)):
    return db.query(ItemDB).filter(ItemDB.name == item_name).all()

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

#Filtering on the basis of price
@router.get("/items_filter")
def filter_items(min_price: float = 0,max_price: float = 1000000,db: Session = Depends(get_db)):
    return db.query(ItemDB).filter(ItemDB.price >= min_price,ItemDB.price <= max_price).all()

#Sorting by price/name where price in ascending is specified as default
@router.get("/items_sort")
def sort_items(order_by: str = "price", db: Session = Depends(get_db)): # price is specify as default parameter

    if order_by == "price":
        return db.query(ItemDB).order_by(ItemDB.price).all() # price ascending
    elif order_by == "-price":
        return db.query(ItemDB).order_by(ItemDB.price.desc()).all() # price descending
    elif order_by == "name":
        return db.query(ItemDB).order_by(ItemDB.name).all() # name ascending
    else:
        return db.query(ItemDB).all() # return as it is 

# Item Search which has given character anywhere in string (API Search)
@router.get("/items_search")
def search_items(char: str, db: Session = Depends(get_db)):
    return db.query(ItemDB).filter(ItemDB.name.ilike(f"%{char}%")).all()
