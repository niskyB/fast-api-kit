from fastapi import APIRouter, Depends, Path, status
from app.schemas.user import UserQueryParams

from app.services import UserService
from dependency_injector.wiring import inject, Provide
from app.core.containers import Container

router = APIRouter()


# @router.get("/{user_id}", status_code=status.HTTP_200_OK)
# @inject
# async def get_user_by_id(
#     user_id: int = Path(..., gt=0),
#     user_service: UserService = Depends(Provide[Container.user_service]),
# ):
#     return await user_service.get_user_by_id(user_id=user_id)


@router.get("/", status_code=status.HTTP_200_OK)
@inject
async def list_users(
    user_service: UserService = Depends(Provide[Container.user_service]),
    params: UserQueryParams = Depends(UserQueryParams),
):
    return await user_service.list_users(params)
