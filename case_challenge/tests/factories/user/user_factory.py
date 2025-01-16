from pydantic import BaseModel
from case_challenge.infra.db.sqlaclhemy.database import get_session_maker
from case_challenge.domains.users.schemas.user_schemas import User as Schema


class UserData(BaseModel):
    email: str
    name: str
    is_active: bool

default_user = UserData(
    name='test_name',
    email='email@email.com',
    is_active=True
)

def create(user: UserData = default_user):
    db = get_session_maker()
    db_user = Schema(
        email=user.email, 
        name=user.name,
        is_active=user.is_active
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_array(amount: int = 1, user: UserData = default_user):
    db = get_session_maker()
    for i in range(amount):
        db_user = Schema(
            email=user.email, 
            name=user.name
        )
        db.add(db_user)

    db.commit()
    db.refresh(db_user)