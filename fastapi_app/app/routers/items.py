from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.item_db import ItemDB # Database Model
from app.models.item_model import Item # Pydantic Model
from app.schemas.item_schema import ItemResponse

from app.services.item_service import (
    create_item_service,
    get_all_items_service,
    get_item_by_id_service,
    update_item_service,
    delete_item_service,
    get_item_by_name_service,
    get_items_paginated_service,
    filter_items_service,
    sort_items_service,
    search_items_service
)

router= APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.post("/items",response_model=ItemResponse)  # Working
def create_item(item: Item, db: Session = Depends(get_db)):
    return create_item_service(db, item)


@router.get("/items",response_model=list[ItemResponse]) # Working
def get_items(db: Session = Depends(get_db)):
    return get_all_items_service(db)


@router.get("/items/{item_id}",response_model=ItemResponse) # Working
def get_item(item_id: int, db: Session = Depends(get_db)):
    return get_item_by_id_service(db, item_id)


@router.put("/items/{item_id}",response_model=ItemResponse)
def update_item(item_id: int, item: Item, db: Session = Depends(get_db)):
    return update_item_service(db, item_id, item)


@router.delete("/items/{item_id}",response_model=ItemResponse)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    return delete_item_service(db, item_id)

@router.get("/items/name/{item_name}",response_model=ItemResponse)
def get_item_by_name(item_name:str, db: Session = Depends(get_db)):
    return get_item_by_name_service(db,item_name)

#Listing Record by specifying limit(how many) and skip ( how many to skip from beginning)
@router.get("/items_paginated",response_model=ItemResponse)
def get_items_paginated(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_items_paginated_service(db,skip,limit)

#Filtering on the basis of price
@router.get("/items_filter",response_model=ItemResponse)
def filter_items(min_price: float = 0,max_price: float = 1000000,db: Session = Depends(get_db)):
    return filter_items_service

#Sorting by price/name where price in ascending is specified as default
@router.get("/items_sort",response_model=ItemResponse)
def sort_items(order_by: str = "price", db: Session = Depends(get_db)): # price is specify as default parameter
    return sort_items_service

# Item Search which has given character anywhere in string (API Search)
@router.get("/items_search")
def search_items(char: str, db: Session = Depends(get_db)):
    return search_items_service
