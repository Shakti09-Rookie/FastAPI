from pydantic import BaseModel

# base model import is required for,
# or it will show error
# pydantic model or schema
class Blog(BaseModel):
    title: str
    body: str


class User(BaseModel):
    Name: str
    email: str
    Age: int
    usr_type: str
    password: str

    # class Config:
    #     orm_mode = True


class ShowUser(BaseModel):
    name: str
    email: str
    # Age: int

    class Config:
        orm_mode = True


class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config:
        orm_mode = True
