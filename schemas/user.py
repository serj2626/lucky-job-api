from pydantic import BaseModel, EmailStr

from enums.user_role import UserRole


class SUserCreate(BaseModel):
    email: EmailStr
    password: str
    role: UserRole


class SUserOut(BaseModel):
    id: str
    email: EmailStr
    role: UserRole
    is_active: bool

    class Config:
        orm_mode = True


class SToken(BaseModel):
    access_token: str
    token_type: str = "bearer"
