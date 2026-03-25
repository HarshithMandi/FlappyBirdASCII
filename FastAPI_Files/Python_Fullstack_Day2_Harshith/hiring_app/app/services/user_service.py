from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.exceptions.custom_exceptions import BadRequestError, ForbiddenError, NotFoundError
from app.models.user import User, UserRole
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate, UserUpdate


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def _hash_password(self, password: str) -> str:
        return pwd_context.hash(password)

    def create_user(self, db: Session, payload: UserCreate) -> User:
        if self.repository.get_by_email(db, payload.email):
            raise BadRequestError("Email already exists")
        user = User(
            name=payload.name,
            email=payload.email,
            role=payload.role,
            hashed_password=self._hash_password(payload.password),
        )
        with db.begin():
            return self.repository.create(db, user)

    def get_user(self, db: Session, user_id: int) -> User:
        user = self.repository.get(db, user_id)
        if not user:
            raise NotFoundError("User not found")
        return user

    def list_users(self, db: Session, skip: int, limit: int) -> list[User]:
        return self.repository.list(db, skip, limit)

    def update_user(self, db: Session, user_id: int, payload: UserUpdate, actor_id: int) -> User:
        actor = self.get_user(db, actor_id)
        if actor.role != UserRole.admin:
            raise ForbiddenError("Only admins can update users")

        user = self.get_user(db, user_id)
        if payload.email and payload.email != user.email:
            if self.repository.get_by_email(db, payload.email):
                raise BadRequestError("Email already exists")
        if payload.name is not None:
            user.name = payload.name
        if payload.email is not None:
            user.email = payload.email
        if payload.role is not None:
            user.role = payload.role
        if payload.password is not None:
            user.hashed_password = self._hash_password(payload.password)
        with db.begin():
            return self.repository.update(db, user)

    def delete_user(self, db: Session, user_id: int, actor_id: int) -> None:
        actor = self.get_user(db, actor_id)
        if actor.role != UserRole.admin:
            raise ForbiddenError("Only admins can delete users")
        user = self.get_user(db, user_id)
        with db.begin():
            self.repository.delete(db, user)
