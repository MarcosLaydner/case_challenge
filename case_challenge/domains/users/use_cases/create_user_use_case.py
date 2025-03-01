from datetime import datetime
from case_challenge.domains.users.models.user_history_models import UserHistoryData
from case_challenge.domains.users.models.user_models import User, UserData
from case_challenge.domains.users.repositories import user_history_repository, user_repository
from case_challenge.errors.basic_error import BasicError


class CreateUserUseCase:
    def __call__(self, user_params: UserData) -> User:
        try:
            user = user_repository.create(user_params)

            if not user:
                raise BasicError(status=400, msg='Unable to create user')

            history = user_history_repository.create(UserHistoryData(
                user_id=user.id,
                email=user.email,
                name=user.name,
                action='create',
                effective_date=datetime.now()
            ))

            if not history:
                raise BasicError(status=400, msg='Unable to create user history')

            return user
        except BasicError as e:
            raise BasicError(status=e.status, msg=e.msg)
        except Exception as e:
            raise BasicError(status=400, msg=str(e))