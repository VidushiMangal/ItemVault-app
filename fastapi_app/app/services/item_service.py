from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.item_db import ItemDB
from app.models.item_model import Item

from app.utils.logging import logger
logger.info("Creating item with name=%s", Item.name)


def create_item_service(db: Session, item: Item): # Working
    db_item = ItemDB(
        name=item.name,
        price=item.price,
        description=item.description
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_all_items_service(db: Session): #Working
    return db.query(ItemDB).all()


def get_item_by_id_service(db: Session, item_id: int): #Working
    item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item with this id not found")
    return item


def update_item_service(db: Session, item_id: int, item: Item): #Working
    db_item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item with id does not exist")
    db_item.name = item.name
    db_item.price = item.price
    db_item.description = item.description
    db.commit()
    db.refresh(db_item)
    return db_item


def delete_item_service(db: Session, item_id: int): #Working
    db_item = db.query(ItemDB).filter(ItemDB.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item with given id does not exist")
    db.delete(db_item)
    db.commit()
    return db_item

def get_item_by_name_service(db: Session, item_name:str ): #Working
    db_items= db.query(ItemDB).filter(ItemDB.name == item_name).all()
    if not db_items:
        raise HTTPException(status_code=400, detail="Item with given name not found")
    return db_items


def get_items_paginated_service(db: Session, skip: int = 0, limit: int = 10 ): #Working
    items = db.query(ItemDB).offset(skip).limit(limit).all()
    return items


def filter_items_service(db: Session, min_price: float = 0,max_price: float = 1000000): #Working
    if min_price<0:
        raise HTTPException(status_code=400,detail="Price cannot be negative")
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

# pagination + filtering + sorting together in a single method
def serach_sort_paging_items_advanced_service(db:Session,skip: int = 0,limit: int = 10,min_price: float = 0,
    max_price: float = 999999,
    order_by: str = "price"
    ):
    query = db.query(ItemDB).filter(ItemDB.price >= min_price,  ItemDB.price <= max_price)
    if order_by == "price":
        query = query.order_by(ItemDB.price)
    elif order_by == "-price":
        query = query.order_by(ItemDB.price.desc())
    elif order_by == "name":
        query = query.order_by(ItemDB.name)

    return query.offset(skip).limit(limit).all()
