from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError
from models import User
from dtos import UserCreate, UserUpdate
from sqlalchemy.orm import sessionmaker

class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_user(self, user_data: UserCreate) -> User:
        user = User(**user_data.dict())
        self.session.add(user)
        try:
            await self.session.commit()
            await self.session.refresh(user)
        except IntegrityError:
            raise ValueError("Username or Email already exists")
        return user

    async def get_user_by_id(self, user_id: int) -> User:
        result = await self.session.execute(select(User).filter_by(id=user_id))
        user = result.scalar_one_or_none()
        return user

    async def update_user(self, user_id: int, user_data: UserUpdate) -> User:
        user = await self.get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        
        for key, value in user_data.dict(exclude_unset=True).items():
            setattr(user, key, value)

        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def delete_user(self, user_id: int) -> None:
        user = await self.get_user_by_id(user_id)
        if not user:
            raise ValueError("User not found")
        
        await self.session.delete(user)
        await self.session.commit()

    async def username_or_email_exists(self, username: str, email: str) -> bool:
        result = await self.session.execute(
            select(User).filter_by(username=username, email=email)
        )
        return result.scalar_one_or_none() is not None
