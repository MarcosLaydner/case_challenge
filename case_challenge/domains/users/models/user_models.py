from pydantic import BaseModel

class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    name: str


class User(UserBase):
    id: int
    is_active: bool
    
    class Config:
        from_attributes = True