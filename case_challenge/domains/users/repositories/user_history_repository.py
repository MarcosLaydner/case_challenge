from case_challenge.domains.users.models.user_history_models import UserHistory, UserHistoryData


from ..schemas.user_history_schemas import UserHistory as Schema
from case_challenge.infra.db.database import SessionLocal


def find_by_user_id(user_id: int):
  db = SessionLocal()
  return db.query(Schema).filter(Schema.user_id == user_id).order_by(Schema.effective_date.desc()).all()


def create(history_data: UserHistoryData) -> UserHistory:
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