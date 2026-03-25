from pydantic import BaseModel, Field


class LoanCreate(BaseModel):
    applicant_name: str = Field(..., min_length=2)
    income: float = Field(..., gt=0)
    loan_amount: float = Field(..., gt=0)


class LoanResponse(LoanCreate):
    id: int
    status: str


class LoanStatusResponse(BaseModel):
    message: str
    status: str
