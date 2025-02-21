from pydantic import BaseModel
from typing import Optional


class BookBase(BaseModel):
    title: str
    author: str
    price: int

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str]= None
    price : Optional[str]= None

class Book(BookBase):
    id: int
    class Config:
        orm_mode = True

#######################################

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: Optional[str] =None
    email: Optional[str] =None

class User(UserBase):
    id: int
    class Config:
        from_attributes = True
