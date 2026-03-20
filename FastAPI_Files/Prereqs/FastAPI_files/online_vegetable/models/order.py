from pydantic import BaseModel
from typing import List, Optional


class Order(BaseModel):
    id: Optional[str] = None
    user_id: str
    product_ids: List[str]
    total: float
    status: str
    