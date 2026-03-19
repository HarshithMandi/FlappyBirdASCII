from app.model.user import User

def create_user(db, user):
    """Create a User from a Pydantic schema instance."""
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db):
    """Return all users from the database."""
    return db.query(User).all()