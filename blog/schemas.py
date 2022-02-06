from turtle import title
from typing import List
from pydantic import BaseModel

# base model import is required for,
# or it will show error
# pydantic model or schema
class BlogBase(BaseModel):
    title: str
    body: str


class Blog(BlogBase):
    class Config:
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    age: int
    usr_type: str
    password: str

    # class Config:
    #     orm_mode = True


class ShowUser(BaseModel):
    name: str
    email: str
    age: int
    blogs: List[Blog] = []

    class Config:
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str
