from models.base import Base
from enums.user_role import UserRole
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Boolean, Enum as SQLEnum


class User(Base):
    __tablename__ = "users"

    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_admin: Mapped[bool] = mapped_column(Boolean, default=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    role: Mapped[UserRole] = mapped_column(SQLEnum(UserRole), nullable=False)