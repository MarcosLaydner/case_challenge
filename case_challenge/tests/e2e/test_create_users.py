from case_challenge.domains.users.repositories import user_history_repository


history_repo = user_history_repository


def test_post_user(test_client):
    response = test_client.post(
        "api/v1/users/",
        json={"name": "bazz", "email": "test@test"},
    )

    result = response.json()

    user_created_history = history_repo.find_by_user_id(result['id'])

    assert len(user_created_history) == 1
    assert user_created_history[0].user_id == result['id']
    assert response.status_code == 201
    assert result == {
        'id': 1,
        "name": "bazz",
        "email": "test@test",
        "is_active": True
    }