from enum import Enum
from datetime import date

from sqlalchemy import Column, Date, Enum as SqlEnum, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.core.database import Base


class PaymentStatus(str, Enum):
    completed = "completed"
    pending = "pending"


class Repayment(Base):
    __tablename__ = "repayments"

    id = Column(Integer, primary_key=True, index=True)
    loan_application_id = Column(Integer, ForeignKey("loan_applications.id"), nullable=False)
    amount_paid = Column(Float, nullable=False)
    payment_date = Column(Date, default=date.today, nullable=False)
    payment_status = Column(SqlEnum(PaymentStatus, name="payment_status"), nullable=False)

    loan_application = relationship("LoanApplication", back_populates="repayments")
