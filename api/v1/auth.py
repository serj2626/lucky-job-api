from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from schemas.user import SUserCreate, UserOut
from services.user_service import create_user

router = APIRouter()


@router.post("/register", response_model=UserOut)
async def register(user_in: SUserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(user_in, db)
