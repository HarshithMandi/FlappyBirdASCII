from enum import Enum

from sqlalchemy import Column, Enum as SqlEnum, Integer, String
from sqlalchemy.orm import relationship

from app.models.base import Base


class UserRole(str, Enum):
    admin = "admin"
    recruiter = "recruiter"
    candidate = "candidate"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    role = Column(SqlEnum(UserRole, name="user_role"), nullable=False)
    hashed_password = Column(String, nullable=False)

    applications = relationship("Application", back_populates="user", cascade="all, delete-orphan")
