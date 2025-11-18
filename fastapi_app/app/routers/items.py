from fastapi import APIRouter

router= APIRouter()

items=[]

@router.get("/items")
def get_item():
    return items

@router.post("/items")
def add_items(item:dict):
    items.append(item)
    return {"msg":"item added","item":item}

@router.get("items/{item_id}")
def get_item(item_id:int):
    if item_id<len(items):
        return items[item_id]
    return("Not Found")

