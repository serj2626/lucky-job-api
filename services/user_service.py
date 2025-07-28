from sqlalchemy.ext.asyncio import AsyncSession
from models.user import User
from schemas.user import UserCreateS
from core.security import hash_password


async def create_user(user_in: UserCreateS, db: AsyncSession) -> User:
    user = User(
        email=user_in.email,
        password_hash=hash_password(user_in.password),
        role=user_in.role,
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
