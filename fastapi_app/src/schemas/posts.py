from pydantic import BaseModel, Field
from typing import List, TYPE_CHECKING, Annotated

if TYPE_CHECKING:
    from src.schemas.categories import Category


class PostBase(BaseModel):
    title: Annotated[str, Field(..., min_length=1, max_length=200)]


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: Annotated[int, Field(ge=1)]
    categories: Annotated[List["Category"], Field(default_factory=list)]

    class Config:
        from_attributes = True
