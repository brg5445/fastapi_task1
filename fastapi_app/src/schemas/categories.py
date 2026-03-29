from pydantic import BaseModel
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from src.schemas.posts import Post


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    posts: List["Post"] = []

    class Config:
        from_attributes = True


