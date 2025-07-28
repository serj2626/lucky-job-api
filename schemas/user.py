from pydantic import BaseModel, EmailStr

from enums.user_role import UserRole


class UserCreateS(BaseModel):
    email: EmailStr
    password: str
    role: UserRole


class UserOutS(BaseModel):
    id: str
    email: EmailStr
    role: UserRole
    is_active: bool

    class Config:
        orm_mode = True


class TokenS(BaseModel):
    access_token: str
    token_type: str = "bearer"
