from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from app.models.base import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    salary = Column(Integer, nullable=False)
    company_id = Column(Integer, nullable=False)

    applications = relationship("Application", back_populates="job", cascade="all, delete-orphan")
