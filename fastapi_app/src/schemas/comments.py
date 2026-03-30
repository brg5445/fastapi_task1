from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Annotated

from src.schemas.posts import Post
from src.schemas.users import User


class CommentBase(BaseModel):
    text: Annotated[str, Field(..., min_length=1, max_length=1000)]


class CommentCreate(CommentBase):
    author_id: Annotated[int, Field(..., ge=1)]
    post_id: Annotated[int, Field(..., ge=1)]


class CommentUpdate(BaseModel):
    text: Annotated[Optional[str], Field(None, min_length=1, max_length=1000)]


class Comment(BaseModel):
    author: User
    post: Post
    text: Annotated[str, Field(..., min_length=1, max_length=1000)]
    created_at: datetime
