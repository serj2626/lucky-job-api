from sqlalchemy.ext.asyncio import AsyncSession

from backend.core.auth import hash_password
from models.user import User
from schemas.user import SUserCreate


async def create_user(user_in: SUserCreate, db: AsyncSession) -> User:
    user = User(
        email=user_in.email,
        password_hash=hash_password(user_in.password),
        role=user_in.role,
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
