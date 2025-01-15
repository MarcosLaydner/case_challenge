from sqlalchemy import Boolean, Column, Integer, String

from ....infra.db.database import Base, engine


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)
    name = Column(String)
    is_active = Column(Boolean, default=True)

Base.metadata.create_all(engine)