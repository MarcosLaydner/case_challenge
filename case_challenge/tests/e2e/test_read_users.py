from case_challenge.tests.factories.user import user_factory


def test_read_user_when_id_does_not_exit(test_client):
    response = test_client.get("api/v1/users/5667")
    assert response.status_code == 404


def test_read_user(test_client):
    user = user_factory.create()
    response = test_client.get(f"api/v1/users/{user.id}")
    assert response.status_code == 200
    assert response.json() == {
        'id': user.id,
        "name": user.name,
        "email": user.email,
        "is_active": user.is_active
    }