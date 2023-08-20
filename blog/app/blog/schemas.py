from typing import List
from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    name: str
    email: str
    password: str

class Blog(BaseModel):
    title: str
    body: str
 
class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[Blog]

class ShowBlog(Blog):
    model_config = ConfigDict(from_attributes=True)
    creator: ShowUser

class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
