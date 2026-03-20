from pydantic import BaseModel, typing
from typing import List, Optional

class Product(BaseModel):
    id: Optional[str] = None
    name: str
    price: float
    stock: int
    
    