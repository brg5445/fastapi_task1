from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Annotated

from src.schemas.users import User


class LocationBase(BaseModel):
    title: Annotated[str, Field(max_length=256)]
    description: Annotated[str, Field(..., min_length=1)]
    is_published: bool


class LocationCreate(LocationBase):
    author_id: Annotated[int, Field(..., ge=1)]


class LocationUpdate(BaseModel):
    title: Annotated[Optional[str], Field(None, max_length=256)]
    description: Annotated[Optional[str], Field(None, min_length=1)]
    is_published: Optional[bool]


class Location(BaseModel):
    id: Annotated[int, Field(ge=1)]
    author: User
    title: Annotated[str, Field(max_length=256)]
    description: Annotated[str, Field(..., min_length=1)]
    is_published: bool
    created_at: datetime
