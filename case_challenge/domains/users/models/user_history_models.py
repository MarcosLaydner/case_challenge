from datetime import datetime
from pydantic import BaseModel

class UserHistoryBase(BaseModel):
    email: str


class UserHistoryData(UserHistoryBase):
    user_id: int
    name: str
    action: str
    effective_date: datetime


class UserHistory(UserHistoryData):
    id: int
    
    class Config:
        from_attributes = True