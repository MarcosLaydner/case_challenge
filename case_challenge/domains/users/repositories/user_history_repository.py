from fastapi import Depends
from sqlalchemy.orm import Session

from case_challenge.domains.users.models.user_history_models import UserHistoryCreate


from ..schemas.user_history_schemas import UserHistory as Schema
from case_challenge.infra.db.database import SessionLocal



# def get_user(user_id: int):
#   db = SessionLocal()
#   return db.query(Schema).filter(Schema.id == user_id).first()


# def get_user_by_email(db: Session, email: str):
#   return db.query(models.User).filter(models.User.email == email).first()




# def get_users(db: Session, skip: int = 0, limit: int = 100):
#   return db.query(models.User).offset(skip).limit(limit).all()


def create(history_data: UserHistoryCreate):
    db = SessionLocal()
    db_user_history = Schema(
        user_id=history_data.user_id,
        email=history_data.email,
        name=history_data.name,
        action=history_data.action,
        effective_date=history_data.effective_date
    )

    db.add(db_user_history)
    db.commit()
    db.refresh(db_user_history)
    return db_user_history