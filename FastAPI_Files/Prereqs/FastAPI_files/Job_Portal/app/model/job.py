from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Job(Base):
    __tablename__="jobs"

    id=Column(Integer,primary_key=True)
    title=Column(String,nullable=False,index=True)
    description=Column(String,nullable=False)

    application=relationship("Application",back_populates="job")
