from pydantic import BaseModel

try:
    # Pydantic v2
    from pydantic import ConfigDict
except ImportError:  # pragma: no cover
    ConfigDict = None

class JobCreate(BaseModel):
    title: str
    description: str

class JobResponse(JobCreate):
    id: int

    if ConfigDict is not None:
        model_config = ConfigDict(from_attributes=True)
    else:  # Pydantic v1
        class Config:
            orm_mode = True