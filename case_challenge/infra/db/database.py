import databases

from contextlib import asynccontextmanager
from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..config.environment import get_settings

SETTINGS = get_settings()

print(SETTINGS)
SQLALCHEMY_DATABASE_URL = f"postgresql://{SETTINGS.DB_USER}:{SETTINGS.DB_PASSWORD}@{SETTINGS.DB_HOST}:{SETTINGS.DB_PORT}/{SETTINGS.DB}"

database = databases.Database(SQLALCHEMY_DATABASE_URL)

metadata = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

@asynccontextmanager
async def database_context():
    await connect_database()
    yield database
    await disconnect_database()


async def connect_database():
    await database.connect()


async def disconnect_database():
    await database.disconnect()


def init_database() -> None:
    metadata.bind = create_engine(SQLALCHEMY_DATABASE_URL)
    global database
    database = databases.Database(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

# def init_test_database() -> None:
#     import moov.infra.db.postgres.models

#     metadata.bind = create_engine(SETTINGS.TEST_DATABASE_URL)
#     global database
#     database = databases.Database(SETTINGS.TEST_DATABASE_URL)
