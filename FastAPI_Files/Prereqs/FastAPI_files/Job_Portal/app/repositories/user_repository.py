from app.model.user import User
from sqlalchemy.exc import IntegrityError

def _schema_to_dict(schema) -> dict:
    if isinstance(schema, dict):
        return schema
    if hasattr(schema, "model_dump"):
        return schema.model_dump()
    return schema.dict()


def create_user(db, user):
    """Create a User from a Pydantic schema instance."""
    payload = _schema_to_dict(user)
    db_user = User(**payload)
    db.add(db_user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise
    db.refresh(db_user)
    return db_user

def get_users(db, skip: int = 0, limit: int = 100):
    """Return users from the database."""
    return db.query(User).offset(skip).limit(limit).all()


def get_user_by_email(db, email: str):
    return db.query(User).filter(User.email == email).first()


def get_user_by_id(db, user_id: int):
    return db.query(User).filter(User.id == user_id).first()