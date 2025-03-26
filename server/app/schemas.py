from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    username: str

class PostCreate(BaseModel):
    content: str

class PostResponse(BaseModel):
    id: int
    content: str
