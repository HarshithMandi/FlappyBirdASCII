from pydantic import BaseModel


class ApplicationCreate(BaseModel):
    user_id: int
    job_id: int