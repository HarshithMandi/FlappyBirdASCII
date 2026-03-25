from enum import Enum

from sqlalchemy import Column, Enum as SqlEnum, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.core.database import Base


class LoanStatus(str, Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"
    disbursed = "disbursed"
    closed = "closed"


class LoanApplication(Base):
    __tablename__ = "loan_applications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("loan_products.id"), nullable=False)
    requested_amount = Column(Float, nullable=False)
    approved_amount = Column(Float, nullable=True)
    status = Column(SqlEnum(LoanStatus, name="loan_status"), default=LoanStatus.pending, nullable=False)
    processed_by = Column(Integer, ForeignKey("users.id"), nullable=True)

    customer = relationship("User", foreign_keys=[user_id], back_populates="loan_applications")
    processor = relationship("User", foreign_keys=[processed_by], back_populates="processed_applications")
    product = relationship("LoanProduct", back_populates="applications")
    repayments = relationship("Repayment", back_populates="loan_application", cascade="all, delete-orphan")
