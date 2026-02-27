from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from schemas.users import User
from schemas.categories import Category


class PostBase(BaseModel):
    text: str
    datetime_to_publish: datetime
    category_id: int


class PostCreate(PostBase):
    author_id: int
    category: Optional[Category] = None
    datetime_to_publish: Optional[datetime] = None

class PostUpdate(BaseModel):
    text: Optional[str]
    category_id: Optional[int]
    datetime_to_publish: Optional[datetime]


class Post(BaseModel):
    id: int
    author: User
    category: Category
    text: str
    datetime_to_publish: datetime
    created_at: datetime


class CategoryBase(BaseModel):
    title: str = Field(max_length=256)
    description: str
    is_published: bool


class CategoryCreate(CategoryBase):
    author_id: int


class CategoryUpdate(BaseModel):
    title: Optional[str] = Field(max_length=256)
    description: Optional[str]
    is_published: Optional[bool]


class Category(BaseModel):
    id: int
    author: User
    title: str = Field(max_length=256)
    description: str
    is_published: bool