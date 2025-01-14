
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from pytest import Session

from case_challenge.domains.users.repositories import user_repository
from ..models.user_models import User, UserCreate


router = APIRouter()
router = APIRouter(default_response_class=JSONResponse)

@router.post("/users/", response_model=User)
async def create_user(user: UserCreate):
    test = user_repository.create_user(user)

    # if db_user:
    #     raise HTTPException(status_code=400, detail="Email already registered")
    return {test}


# @router.get("/users/", response_model=list[User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = actions.get_users(db, skip=skip, limit=limit)
#     return users


# @router.get("/users/{user_id}", response_model=User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = actions.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user