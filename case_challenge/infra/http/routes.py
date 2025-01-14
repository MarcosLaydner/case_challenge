from fastapi import FastAPI

from case_challenge.domains.application.controllers import application_controller
from case_challenge.domains.users.controllers import user_controller


def register_routers(app: FastAPI) -> FastAPI:
    app.include_router(application_controller.router, tags=['Application'])
    app.include_router(user_controller.router, prefix="/api/v1", tags=['Users'])
    return app