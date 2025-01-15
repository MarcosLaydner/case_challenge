from fastapi import FastAPI

from case_challenge.infra.db.database import connect_database, disconnect_database
from case_challenge.infra.db.database import (
    init_database as init_pgsql_db,
    # init_test_database as init_test_pgsql_db,
)
from toolz import pipe

from case_challenge.infra.http.routes import register_routers

def create_instance() -> FastAPI:
    return FastAPI()


def init_databases() -> FastAPI:
    init_pgsql_db()

# def init_test_databases(app: FastAPI) -> FastAPI:
#     init_test_pgsql_db()
#     return app


# def register_events(app: FastAPI) -> FastAPI:
#     print(app)
#     app.on_event("startup")(connect_database)
#     app.on_event("shutdown")(disconnect_database)

#     return app


# def register_middlewares(app: FastAPI) -> FastAPI:
#     cors_middleware(app)
#     return app


def init_app() -> FastAPI:
    app = create_instance()
    return register_routers(app)


# def init_test_app(settings: Settings) -> FastAPI:
#     app: FastAPI = pipe(
#         settings,
#         create_instance,
#         init_test_databases,
#         register_events,
#         # register_middlewares,
#         register_routers,
#     )
#     return app
