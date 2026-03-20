from pydantic import BaseModel
from typing import List, Optional

class ProductCreate(BaseModel):
    name: str
    price: float
    stock: int

class ProductOut(BaseModel):
    id: str
    name: str
    price: float
    stock: int