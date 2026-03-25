from pydantic import BaseModel, Field


class CourseCreate(BaseModel):
    title: str = Field(..., min_length=2)
    duration: int = Field(..., gt=0)


class CourseResponse(CourseCreate):
    id: int
