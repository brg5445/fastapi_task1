from pydantic import BaseModel
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from src.schemas.categories import Category


class PostBase(BaseModel):
    title: str


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    categories: List["Category"] = []

    class Config:
        from_attributes = True
