from enum import Enum

from fastapi import status
from fastapi.routing import APIRouter
from pydantic import BaseModel, Field

router = APIRouter()


class StatusEnum(str, Enum):
    OK = "OK"
    FAILURE = "FAILURE"
    CRITICAL = "CRITICAL"
    UNKNOWN = "UNKNOWN"


class HealthCheck(BaseModel):
    status: StatusEnum = Field(..., description="API current status")


@router.get(
    "/status",
    response_model=HealthCheck,
    status_code=status.HTTP_200_OK,
    summary="Performs health check",
    description="Performs health check and returns information about running service.",
)
async def health_check():
    return {
        "status": StatusEnum.OK,
    }
