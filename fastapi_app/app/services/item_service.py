from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.item_db import ItemDB
from app.models.item_model import Item

def create_item_service(db: Session, item: Item):
    db_item = ItemDB(
        name=item.name,
        price=item.price,
        description=item.description
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_all_items_service(db: Session):
    return db.query(ItemDB).all()


def get_item_by_id_service(db: Session, item_id: int):
    item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


def update_item_service(db: Session, item_id: int, item: Item):
    db_item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.name = item.name
    db_item.price = item.price
    db_item.description = item.description
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item_service(db: Session, item_id: int):
    db_item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(db_item)
    db.commit()
    return {"msg": "Item deleted"}

def get_item_by_name_service(db: Session, item_name:str ):
    return db.query(ItemDB).filter(ItemDB.name == item_name).all()


def get_items_paginated_service(db: Session, skip: int = 0, limit: int = 10 ):
    items = db.query(ItemDB).offset(skip).limit(limit).all()
    return items

def filter_items_service(db: Session, min_price: float = 0,max_price: float = 1000000):
    return db.query(ItemDB).filter(ItemDB.price >= min_price,ItemDB.price <= max_price).all()

def sort_items_service(db: Session, order_by: str = "price" ): # price is specify as default parameter
    if order_by == "price":
        return db.query(ItemDB).order_by(ItemDB.price).all() # price ascending
    elif order_by == "-price":
        return db.query(ItemDB).order_by(ItemDB.price.desc()).all() # price descending
    elif order_by == "name":
        return db.query(ItemDB).order_by(ItemDB.name).all() # name ascending
    else:
        return db.query(ItemDB).all() # return as it is 

# Item Search which has given character anywhere in string (API Search)
def search_items_service(db: Session, char: str):
    return db.query(ItemDB).filter(ItemDB.name.ilike(f"%{char}%")).all()
