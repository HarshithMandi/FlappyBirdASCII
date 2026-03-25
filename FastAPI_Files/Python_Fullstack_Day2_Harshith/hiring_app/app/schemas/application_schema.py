from pydantic import BaseModel

from app.models.application import ApplicationStatus


class ApplicationBase(BaseModel):
    user_id: int
    job_id: int


class ApplicationCreate(ApplicationBase):
    pass


class ApplicationStatusUpdate(BaseModel):
    status: ApplicationStatus
    processed_by: int


class ApplicationResponse(ApplicationBase):
    id: int
    status: ApplicationStatus

    model_config = {"from_attributes": True}
