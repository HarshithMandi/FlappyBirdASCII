from pydantic import BaseModel, typing
from typing import List, Optional
    
class User(BaseModel):
    id: Optional[str] = None
    username: str
    email: str
    hashed_password: str
    role: str
    