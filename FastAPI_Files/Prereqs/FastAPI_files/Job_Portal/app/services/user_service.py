from app.repositories import user_repository
def create_user_service(db, user: dict):
    return user_repository.create_user(db, user)
def get_users_service(db):
    return user_repository.get_users(db)