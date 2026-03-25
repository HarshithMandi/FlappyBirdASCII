from datetime import date

from pydantic import BaseModel

from app.models.repayment import PaymentStatus


class RepaymentCreate(BaseModel):
    loan_application_id: int
    amount_paid: float
    payment_date: date | None = None
    payment_status: PaymentStatus = PaymentStatus.completed


class RepaymentOut(BaseModel):
    id: int
    loan_application_id: int
    amount_paid: float
    payment_date: date
    payment_status: PaymentStatus

    model_config = {"from_attributes": True}
