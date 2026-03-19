from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base

class Application(Base):
    __tablename__="applications"

    id=Column(Integer,primary_key=True)
    user_id=Column(Integer, ForeignKey("users.id"), nullable=False)
    job_id=Column(Integer, ForeignKey("jobs.id"), nullable=False)
    
    user=relationship("User",back_populates="application")
    job=relationship("Job",back_populates="application")
