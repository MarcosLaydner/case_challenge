from case_challenge.infra.db.database import SessionLocal

from case_challenge.domains.users.models.user_models import UserData
from ..schemas.user_schemas import User as Schema


def find_by_id(id: int):
  db = SessionLocal()
  return db.query(Schema).filter(Schema.id == id, Schema.is_active == True).first()


def soft_delete(id: int):
  db = SessionLocal()

  db.query(Schema).filter(Schema.id == id).update({
       'is_active': False,
    })
  db.commit()


def find_by(filters: UserData, page: int = 0, per_page: int = 100):
  db = SessionLocal()
  return db.query(Schema).filter_by(**filters).offset(page).limit(per_page)


def update(id: int, user: UserData):
    db = SessionLocal()

    db.query(Schema).filter(Schema.id == id).update({
       'name': user.name,
       'email': user.email
    })

    db.commit()

def create(user: UserData):
    db = SessionLocal()
    db_user = Schema(
        email=user.email, 
        name=user.name
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user