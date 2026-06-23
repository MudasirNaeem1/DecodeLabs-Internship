from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UserRegister(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, example="Mudasir Ahmed")
    email: EmailStr = Field(..., example="mudasir@example.com")
    password: str = Field(..., min_length=6, example="securepass123")

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=50)

class UserPublic(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool

    class Config:
        from_attributes = True

class UserInDB(BaseModel):
    id: int
    name: str
    email: str
    hashed_password: str
    is_active: bool = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    email: Optional[str] = None
