


from case_challenge.tests.factories.user import user_factory


def test_list_users_when_no_users(test_client):
    response = test_client.get("api/v1/users/")
    assert response.status_code == 200
    assert response.json() == []


def test_list_users_when_they_exist(test_client):
    user_factory.create_array(3)
    response = test_client.get("api/v1/users/")
    assert response.status_code == 200
    assert len(response.json()) == 3


def test_list_users_should_ignore_inactive_users(test_client):
    user_factory.create_array(3)
    user_factory.create(user_factory.UserData(
    name='test_name',
    email='email@email.com',
    is_active=False
))
    response = test_client.get("api/v1/users/")
    assert response.status_code == 200
    assert len(response.json()) == 3