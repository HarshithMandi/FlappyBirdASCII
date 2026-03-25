from pydantic import BaseModel, EmailStr, Field


class StudentCreate(BaseModel):
    name: str = Field(..., min_length=2)
    email: EmailStr


class StudentResponse(StudentCreate):
    id: int
