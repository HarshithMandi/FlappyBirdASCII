from pydantic import BaseModel


class JobBase(BaseModel):
    title: str
    description: str
    salary: int
    company_id: int


class JobCreate(JobBase):
    pass


class JobUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    salary: int | None = None
    company_id: int | None = None


class JobResponse(JobBase):
    id: int

    model_config = {"from_attributes": True}
