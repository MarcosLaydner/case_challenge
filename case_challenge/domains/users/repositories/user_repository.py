from fastapi import Depends
from sqlalchemy.orm import Session

from case_challenge.domains.users.models.user_models import UserCreate


from ..schemas.user_schemas import User as Schema
from case_challenge.infra.db.database import SessionLocal



def get_user(user_id: int):
  db = SessionLocal()
  return db.query(Schema).filter(Schema.id == user_id).first()


# def get_user_by_email(db: Session, email: str):
#   return db.query(models.User).filter(models.User.email == email).first()




# def get_users(db: Session, skip: int = 0, limit: int = 100):
#   return db.query(models.User).offset(skip).limit(limit).all()


def create(user: UserCreate):
    db = SessionLocal()
    db_user = Schema(
        email=user.email, 
        name=user.name
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user