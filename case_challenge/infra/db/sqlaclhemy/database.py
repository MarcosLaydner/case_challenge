from sqlalchemy import Engine, MetaData, create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from ...config.environment import get_settings

Base = declarative_base()

class Database:
    engine = None
    session_maker = None

    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance

db_instance = Database()

SETTINGS = get_settings()

SQLALCHEMY_DATABASE_URL = f"postgresql://{SETTINGS.DB_USER}:{SETTINGS.DB_PASSWORD}@{SETTINGS.DB_HOST}:{SETTINGS.DB_PORT}/{SETTINGS.DB}"
SQLALCHEMY_TEST_DATABASE_URL = f"postgresql://{SETTINGS.DB_USER}:{SETTINGS.DB_PASSWORD}@{SETTINGS.DB_HOST}:{SETTINGS.DB_PORT}/{SETTINGS.TEST_DB}"


def get_session_maker() -> Session:
    if not db_instance.session_maker:
        db_instance.session_maker = sessionmaker(autocommit=False, autoflush=False, bind=db_instance.engine)
    return db_instance.session_maker()


def start_engine(db_url: str) -> None:
    db_instance.engine = create_engine(db_url)
    db_instance.session_maker = sessionmaker(autocommit=False, autoflush=False, bind=db_instance.engine)


def get_engine() -> Engine:
    if not db_instance.engine:
        start_engine(SQLALCHEMY_DATABASE_URL)
    
    return db_instance.engine


def init_database() -> None:
    start_engine(SQLALCHEMY_DATABASE_URL)


def init_test_database() -> None:
    start_engine(SQLALCHEMY_TEST_DATABASE_URL)

def clear_test_database() -> None:
    Base.metadata.drop_all(get_engine())
    Base.metadata.create_all(get_engine())
