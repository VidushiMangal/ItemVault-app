from pydantic import BaseModel

class ItemResponse(BaseModel):
    id: int
    name: str
    price: float
    description: str | None

    class Config:
        orm_mode = True #allows Pydantic to read SQLAlchemy objects & convert into JSON-compatible format
