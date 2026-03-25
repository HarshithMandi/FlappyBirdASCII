from sqlalchemy import Column, Float, Integer, String, Text
from sqlalchemy.orm import relationship

from app.core.database import Base


class LoanProduct(Base):
    __tablename__ = "loan_products"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, unique=True, nullable=False)
    interest_rate = Column(Float, nullable=False)
    max_amount = Column(Float, nullable=False)
    tenure_months = Column(Integer, nullable=False)
    description = Column(Text, nullable=True)

    applications = relationship("LoanApplication", back_populates="product")
