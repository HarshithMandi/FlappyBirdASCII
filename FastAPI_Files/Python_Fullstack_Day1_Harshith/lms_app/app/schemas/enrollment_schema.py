from pydantic import BaseModel, Field


class EnrollmentCreate(BaseModel):
    student_id: int = Field(..., gt=0)
    course_id: int = Field(..., gt=0)


class EnrollmentResponse(EnrollmentCreate):
    id: int


class StudentEnrollmentResponse(BaseModel):
    course_id: int
    course_title: str
