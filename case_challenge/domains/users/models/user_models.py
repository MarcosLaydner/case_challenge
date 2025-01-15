from pydantic import BaseModel

from case_challenge.domains.users.models.user_history_models import UserHistory

class UserBase(BaseModel):
    email: str


class UserData(UserBase):
    name: str

class User(UserData):
    id: int
    is_active: bool
    
    class Config:
        from_attributes = True

class AuditUser(User):
    history: list[UserHistory]