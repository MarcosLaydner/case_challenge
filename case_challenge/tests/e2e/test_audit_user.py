from datetime import datetime
from case_challenge.tests.factories.user import user_factory, user_history_factory


def test_audit_user_when_id_does_not_exit(test_client):
    response = test_client.get("api/v1/users/5667/audit")
    assert response.status_code == 404


def test_audit_user(test_client):
    user = user_factory.create()
    user_history = user_history_factory.create(user_history_factory.UserHistoryData(
        email=user.email, 
        name=user.name,
        action='create',
        effective_date=datetime.now(),
        user_id=user.id
    ))

    response = test_client.get(f"api/v1/users/{user.id}/audit")
    assert response.status_code == 200
    assert response.json() == {
        'id': user.id,
        "name": user.name,
        "email": user.email,
        "is_active": user.is_active,
        "history": [
            {
                'id': user_history.id,
                "name": user.name,
                "email": user.email,
                'user_id': user.id,
                'action': user_history.action,
                'effective_date': user_history.effective_date.isoformat()
            }
        ]
    }