from enum import Enum

from sqlalchemy import Column, Enum as SqlEnum, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class UserRole(str, Enum):
    admin = "admin"
    loan_officer = "loan_officer"
    customer = "customer"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    role = Column(SqlEnum(UserRole, name="user_role"), nullable=False)
    hashed_password = Column(String, nullable=False)

    loan_applications = relationship(
        "LoanApplication",
        back_populates="customer",
        foreign_keys="LoanApplication.user_id",
    )
    processed_applications = relationship(
        "LoanApplication",
        back_populates="processor",
        foreign_keys="LoanApplication.processed_by",
    )
