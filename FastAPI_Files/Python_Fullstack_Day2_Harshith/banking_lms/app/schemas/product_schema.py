from pydantic import BaseModel


class LoanProductBase(BaseModel):
    product_name: str
    interest_rate: float
    max_amount: float
    tenure_months: int
    description: str | None = None


class LoanProductCreate(LoanProductBase):
    pass


class LoanProductUpdate(BaseModel):
    product_name: str | None = None
    interest_rate: float | None = None
    max_amount: float | None = None
    tenure_months: int | None = None
    description: str | None = None


class LoanProductOut(LoanProductBase):
    id: int

    model_config = {"from_attributes": True}
