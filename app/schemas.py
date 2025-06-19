from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class PostBase(BaseModel):
    content: str
    image_url: Optional[str] = None

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    likes: int
    owner_id: int
    created_at: datetime

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    posts: List[Post] = []

    class Config:
        from_attributes = True
