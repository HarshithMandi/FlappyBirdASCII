from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

engine=create_engine(
    settings.DATABASE_URL,
    echo=settings.DEBUG,
    future=True
)

Sessionlocal=sessionmaker(bind=engine,autocommit=False,autoflush=False)

Base=declarative_base()

def get_db():
    db=Sessionlocal()
    try:
        yield db
    finally:
        db.close()