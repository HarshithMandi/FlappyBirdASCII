from pydantic import BaseModel
from typing import List, Optional

class OrderCreate(BaseModel):
    user_id: str
    product_ids: List[str]
    total: float
    
class OrderOut(BaseModel):
    id: str
    user_id: str
    product_ids: List[str]
    total: float
    status: str