from datetime import datetime
from pydantic import BaseModel
from case_challenge.infra.db.sqlaclhemy.database import get_session_maker
from case_challenge.domains.users.schemas.user_history_schemas import UserHistory as Schema


class UserHistoryData(BaseModel):
    email: str
    name: str
    action: str
    effective_date: datetime
    user_id: int

default_history = UserHistoryData(
    name='test_name',
    email='email@email.com',
    action='update',
    effective_date=datetime.now(),
    user_id=1
)

def create(data: UserHistoryData = default_history):
    db = get_session_maker()
    db_history = Schema(
        email=data.email, 
        name=data.name,
        action=data.action,
        effective_date=data.effective_date,
        user_id=data.user_id
    )

    db.add(db_history)
    db.commit()
    db.refresh(db_history)
    return db_history


def create_array(amount: int = 1, data: UserHistoryData = default_history):
    db = get_session_maker()
    for i in range(amount):
        db_history = Schema(
        email=data.email, 
        name=data.name,
        action=data.action,
        effective_date=data.effective_date,
        user_id=data.user_id
    )
        db.add(db_history)

    db.commit()
    db.refresh(db_history)