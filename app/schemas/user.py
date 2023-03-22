from typing import List, Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class UserUpdate(UserBase):
    password: Optional[str]


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserList(BaseModel):
    __root__: List[User]
