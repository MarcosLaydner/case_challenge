from datetime import datetime
from case_challenge.domains.users.models.user_history_models import UserHistoryData
from case_challenge.domains.users.models.user_models import User
from case_challenge.domains.users.repositories import user_history_repository, user_repository
from case_challenge.errors.basic_error import BasicError


class DeleteUserUseCase:
    def __call__(self, user_id: int) -> User:
        try:
            user = user_repository.find_by_id(user_id)
            if not user:
                raise BasicError(status=404, msg='User not found')

            user_repository.soft_delete(user_id)

            history = user_history_repository.create(UserHistoryData(
                user_id=user.id,
                email=user.email,
                name=user.name,
                action='delete',
                effective_date=datetime.now()
            ))

            if not history:
                raise BasicError(status=400, msg='Unable to create user history')

            return
        except BasicError as e:
            raise BasicError(status=e.status, msg=e.msg)
        except Exception as e:
            raise BasicError(msg=str(e))