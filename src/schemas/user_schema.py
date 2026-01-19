from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from enum import Enum

# Fallback for EmailStr to avoid dependency issues
EmailStr = str


class UserRole(str, Enum):
    ADMIN = "admin"
    CUSTOMER = "customer"

class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr

class UserCreate(UserBase):
    password: str = Field(..., min_length=6)
    role: Optional[UserRole] = UserRole.CUSTOMER

class UserResponse(UserBase):
    id: int
    role: UserRole
    created_at: datetime

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str
