from pydantic import BaseModel

class Item(BaseModel):  # Pydantic Model=API Layer
    name: str
    price: float
    description: str | None = None
