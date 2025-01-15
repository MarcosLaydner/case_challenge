from case_challenge.domains.users.models.user_models import User
from case_challenge.domains.users.repositories import  user_repository
from case_challenge.errors.basic_error import BasicError


class ReadUserUseCase:
    def __call__(self, user_id: int) -> User:
        try:
            user = user_repository.find_by_id(user_id)

            return user
        except Exception as e:
            raise BasicError(msg=str(e))