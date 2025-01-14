import os
import sys

import uvicorn

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from case_challenge.api.app import init_app
from case_challenge.infra.config.environment import get_settings


web_app = init_app()


def start_web_server() -> None:
    settings = get_settings()
    uvicorn.run(
        "main:web_app",
        host=settings.WEB_SERVER_HOST,
        port=settings.WEB_SERVER_PORT,
        reload=settings.WEB_SERVER_RELOAD,
    )


if __name__ == '__main__':
    start_web_server()
