from pydantic import BaseModel

try:
    # Pydantic v2
    from pydantic import ConfigDict
except ImportError:  # pragma: no cover
    ConfigDict = None


class ApplicationCreate(BaseModel):
    user_id: int
    job_id: int


class ApplicationResponse(ApplicationCreate):
    id: int

    if ConfigDict is not None:
        model_config = ConfigDict(from_attributes=True)
    else:  # Pydantic v1
        class Config:
            orm_mode = True