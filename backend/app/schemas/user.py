from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    bio: Optional[str] = ""

class UserOut(BaseModel):
    id: int
    username: str
    first_name: str
    last_name: str
    email: EmailStr
    bio: Optional[str]
    profile_image_url: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
