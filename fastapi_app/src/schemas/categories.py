from pydantic import BaseModel, Field
from typing import List, TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from src.schemas.posts import Post


class CategoryBase(BaseModel):
    name: Annotated[str, Field(..., min_length=1, max_length=100)]


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: Annotated[int, Field(ge=1)]
    posts: Annotated[List["Post"], Field(default_factory=list)]

    class Config:
        from_attributes = True
