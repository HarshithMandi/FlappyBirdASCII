from repositories.user_repository import UserRepository
from models.user import User
from schemas.user_schema import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def create_user(self, user_data: UserCreate) -> str:
        hashed_password = pwd_context.hash(user_data.password)
        user = User(
            username=user_data.username,
            email=user_data.email,
            hashed_password=hashed_password,
            role="user"
        )
        return await self.user_repository.create(user)

    async def get_user_by_email(self, email: str) -> User:
        return await self.user_repository.get_by_email(email)