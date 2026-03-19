from pydantic import BaseModel

try:
    # Pydantic v2
    from pydantic import ConfigDict
except ImportError:  # pragma: no cover
    ConfigDict = None

class UserCreate(BaseModel):
    name: str
    email: str

class UserResponse(UserCreate):
    id: int

    if ConfigDict is not None:
        model_config = ConfigDict(from_attributes=True)
    else:  # Pydantic v1
        class Config:
            orm_mode = True

