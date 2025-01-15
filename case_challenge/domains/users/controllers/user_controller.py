
from fastapi import APIRouter, HTTPException, Response, status
from fastapi.responses import JSONResponse

from case_challenge.domains.users.use_cases.audit_user_use_case import AuditUserUseCase
from case_challenge.domains.users.use_cases.create_user_use_case import CreateUserUseCase
from case_challenge.domains.users.use_cases.delete_user_use_case import DeleteUserUseCase
from case_challenge.domains.users.use_cases.list_users_use_case import ListUsersUseCase
from case_challenge.domains.users.use_cases.read_user_use_case import ReadUserUseCase
from case_challenge.domains.users.use_cases.update_user_use_case import UpdateUserUseCase
from case_challenge.errors.basic_error import BasicError
from ..models.user_models import AuditUser, User, UserData


router = APIRouter()
router = APIRouter(default_response_class=JSONResponse)


@router.get(
    "/users/",
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "User data", "model": list[User]},
    }
)
def list_users(page: int = 0, per_page: int = 100):
    try:
        return ListUsersUseCase()(page, per_page)
    except BasicError as e:
        raise HTTPException(status_code=e.status, detail=e.msg)


@router.post(
    "/users/",
    status_code=status.HTTP_201_CREATED,
    responses={
        201: {"description": "User registered", "model": User},
    }
)
async def create_user(user: UserData):
    try:
        return CreateUserUseCase()(user)
    except BasicError as e:
        raise HTTPException(status_code=e.status, detail=e.msg)


@router.patch(
    "/users/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": "User updated", "model": None},
        404: {"description": "User not found", "model": None},
    }
)
def update_user(user_id: int, user: UserData):
    try:
        UpdateUserUseCase()(user_id, user)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except BasicError as e:
        raise HTTPException(status_code=e.status, detail=e.msg)


@router.delete(
    "/users/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    responses={
        204: {"description": "User deleted", "model": None},
        404: {"description": "User not found", "model": None},
    }
)
def delete_user(user_id: int):
    try:
        DeleteUserUseCase()(user_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except BasicError as e:
        raise HTTPException(status_code=e.status, detail=e.msg)


@router.get(
    "/users/{user_id}",
    status_code=status.HTTP_200_OK,
    responses={
        200: {"description": "User Data", "model": User},
        404: {"description": "User not found", "model": None},
    }
)
def read_user(user_id: int):
    db_user = ReadUserUseCase()(user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/users/{user_id}/audit", response_model=AuditUser)
def audit_user(user_id: int):
    try:
        db_user = AuditUserUseCase()(user_id)
        if not db_user:
            raise HTTPException(status_code=404, detail="User not found")
        return db_user
    except BasicError as e:
        raise HTTPException(status_code=e.status, detail=e.msg)