from pydantic import BaseModel, SecretStr, Field
from datetime import datetime
from typing import Optional, Annotated


class UserBase(BaseModel):
    login: Annotated[str, Field(..., min_length=3, max_length=50, pattern=r"^[a-zA-Z0-9_]+$")]


class UserCreate(UserBase):
    password: Annotated[SecretStr, Field(..., min_length=6)]


class UserUpdate(BaseModel):
    login: Annotated[Optional[str], Field(None, min_length=3, max_length=50, pattern=r"^[a-zA-Z0-9_]+$")]
    password: Annotated[Optional[SecretStr], Field(None, min_length=6)]


class User(UserBase):
    id: Annotated[int, Field(ge=1)]
    created_at: datetime
