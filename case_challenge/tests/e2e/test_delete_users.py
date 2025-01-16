from case_challenge.domains.users.repositories import user_history_repository
from case_challenge.tests.factories.user import user_factory


history_repo = user_history_repository

def test_delete_user_when_id_does_not_exit(test_client):
    response = test_client.delete("api/v1/users/5667")
    assert response.status_code == 404


def test_delete_user(test_client):
    user = user_factory.create()

    response = test_client.delete(f"api/v1/users/{user.id}")

    user_delete_history = history_repo.find_by_user_id(user.id)

    assert user_delete_history[0].user_id == user.id
    assert response.status_code == 204