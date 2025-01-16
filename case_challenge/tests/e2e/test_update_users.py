from case_challenge.domains.users.repositories import user_history_repository, user_repository
from case_challenge.tests.factories.user import user_factory


history_repo = user_history_repository
user_repo = user_repository

def test_update_user_when_id_does_not_exit(test_client):
    response = test_client.patch(
        "api/v1/users/5667",
        json={"name": "bazz", "email": "test@test"},
    )
    assert response.status_code == 404


def test_update_user(test_client):
    user = user_factory.create()

    response = test_client.patch(
        f"api/v1/users/{user.id}",
        json={"name": "bazz", "email": "test@test"},
    )

    updated_user = user_repo.find_by_id(user.id)

    user_update_history = history_repo.find_by_user_id(updated_user.id)

    assert updated_user.name == 'bazz'
    assert updated_user.email == 'test@test'
    assert user_update_history[0].user_id == user.id
    assert response.status_code == 204