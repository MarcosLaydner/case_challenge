import pytest
from sqlalchemy.orm import session

from fastapi.testclient import TestClient

from case_challenge.api.app import init_test_app
from case_challenge.infra.db.sqlaclhemy.database import clear_test_database, get_session_maker

@pytest.fixture(scope='class')
def web_app():
    return init_test_app()


@pytest.fixture()
def test_client(web_app):
    session.close_all_sessions()
    clear_test_database()
    return TestClient(web_app)