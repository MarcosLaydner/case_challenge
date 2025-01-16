from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from case_challenge.domains.users.schemas.user_schemas import User

from ....infra.db.sqlaclhemy.database import Base, get_engine


class UserHistory(Base):
    __tablename__ = "users_history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(User.id), index=True)
    email = Column(String)
    name = Column(String)
    action = Column(String)
    effective_date = Column(DateTime)

    user = relationship('User', foreign_keys='UserHistory.user_id')


Base.metadata.create_all(get_engine())