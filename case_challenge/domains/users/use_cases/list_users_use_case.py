from case_challenge.domains.users.models.user_models import User
from case_challenge.domains.users.repositories import user_repository
from case_challenge.errors.basic_error import BasicError


class ListUsersUseCase:
    def __call__(self, page: int, per_page: int, filters = {}) -> User:
        try:
            filters['is_active'] = True
            return user_repository.find_by(filters, page, per_page)
        except Exception as e:
            raise BasicError(msg=str(e))