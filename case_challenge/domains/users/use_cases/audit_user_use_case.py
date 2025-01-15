from case_challenge.domains.users.models.user_models import AuditUser, User
from case_challenge.domains.users.repositories import user_history_repository, user_repository
from case_challenge.errors.basic_error import BasicError


class AuditUserUseCase:
    def __call__(self, user_id: int) -> User:
        try:
            user = user_repository.find_by_id(user_id)

            if not user:
                return

            history = user_history_repository.find_by_user_id(user_id)

            user = AuditUser(
                id=user.id,
                name=user.name,
                email=user.email,
                is_active=user.is_active,
                history=history
            )

            return user
        except Exception as e:
            raise BasicError(msg=str(e))