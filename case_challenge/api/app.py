from fastapi import FastAPI

from case_challenge.infra.db.sqlaclhemy.database import (
    init_database,
    init_test_database,
)
from case_challenge.infra.http.routes import register_routers

def init_app() -> FastAPI:
    app = FastAPI()
    init_database()
    return register_routers(app)


def init_test_app() -> FastAPI:
    app = FastAPI()
    init_test_database()
    return register_routers(app)
