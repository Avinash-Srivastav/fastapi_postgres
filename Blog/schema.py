from pydantic import BaseModel
from typing import Optional, List

class BlogCreate(BaseModel):
    title: str
    body: str
    user_id: int

    class Config:
        orm_mode = True

class Blog(BlogCreate):
    class Config:
        orm_mode = True

class ShowBlog(BaseModel):
    id: int
    title: str
    body: str
    user : 'ShowUser'

    class Config:
        orm_mode = True


class UpdateBlog(BaseModel):
    title : Optional[int] = None
    body : Optional[str] = None


class UserCreate(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        from_attributes = True



class User(BaseModel):
    id: int
    name: str
    email: str
    password: str

    class Config:
        orm_mode = True



class ShowUser(BaseModel):
    id: int
    name: str
    email: str
    blogs: Optional[List[ShowBlog]]

    class Config:
        orm_mode = True



class Login(BaseModel):
    username :str  
    password : str



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None   