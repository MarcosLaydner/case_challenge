from fastapi import FastAPI

from case_challenge.domains.application.controllers import application_controller


def register_routers(app: FastAPI) -> FastAPI:
    app.include_router(application_controller.router)
    return app