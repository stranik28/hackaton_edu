from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from api.depends.pagination import PagesPaginationParams
from api.response.user import ResponseUser
from api.response.user import ResponseUserTechFactory
from api.request.user import RequestUser
from api.response.base import ResponseEmpty

from db.models.user import User

from database import get_async_session

from managers.user import UserManager

router = APIRouter(prefix='/user', tags=['User'])


@router.get('/tech', response_model=list[ResponseUser])
async def all_user(
        pagination: PagesPaginationParams = Depends(),
        session: AsyncSession = Depends(get_async_session)
):
    users: list[User] = await UserManager.get_all(
        limit=pagination.limit,
        offset=pagination.offset,
        session=session
    )
    return ResponseUserTechFactory.from_models(users=users)


@router.post('/', response_model=ResponseEmpty)
async def create_user(
        request: RequestUser,
        session: AsyncSession = Depends(get_async_session)
):
    await UserManager.create(
        user=request,
        session=session
    )

    return ResponseEmpty()
