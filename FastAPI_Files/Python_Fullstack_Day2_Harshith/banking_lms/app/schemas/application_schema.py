from pydantic import BaseModel

from app.models.loan_application import LoanStatus


class LoanApplicationBase(BaseModel):
    user_id: int
    product_id: int
    requested_amount: float


class LoanApplicationCreate(LoanApplicationBase):
    pass


class LoanApplicationStatusUpdate(BaseModel):
    status: LoanStatus
    processed_by: int
    approved_amount: float | None = None


class LoanApplicationOut(BaseModel):
    id: int
    user_id: int
    product_id: int
    requested_amount: float
    approved_amount: float | None = None
    status: LoanStatus
    processed_by: int | None = None

    model_config = {"from_attributes": True}
