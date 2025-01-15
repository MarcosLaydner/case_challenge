from datetime import datetime
from pydantic import BaseModel

class UserHistoryBase(BaseModel):
    email: str


class UserHistoryCreate(UserHistoryBase):
    user_id: int
    name: str
    action: str
    effective_date: datetime


class UserHistory(UserHistoryBase):
    id: int
    is_active: bool
    
    class Config:
        from_attributes = True