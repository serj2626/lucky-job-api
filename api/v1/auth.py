from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.user import UserCreate, UserOut
from app.db.session import get_db
from services.user_service import create_user

router = APIRouter()


@router.post("/register", response_model=UserOut)
async def register(user_in: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(user_in, db)
