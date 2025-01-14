from fastapi import Depends
from sqlalchemy.orm import Session

from case_challenge.domains.users.models.user_models import UserCreate


from ..schemas.user_schemas import User as Model
from case_challenge.infra.db.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# def get_user(db: Session, user_id: int):
#   return db.query(models.User).filter(models.User.id == user_id).first()




# def get_user_by_email(db: Session, email: str):
#   return db.query(models.User).filter(models.User.email == email).first()




# def get_users(db: Session, skip: int = 0, limit: int = 100):
#   return db.query(models.User).offset(skip).limit(limit).all()


def create_user(user: UserCreate):
    db = SessionLocal()
    db_user = Model(
        email=user.email, 
        name=user.name
        )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user