from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from api.depends.pagination import PagesPaginationParams
from api.response.university import ResponseUniversity

from database import get_async_session

from managers.university import UniversityManager

router = APIRouter(prefix='/university', tags=['University'])


@router.get('/')
async def all_university(
        pagination: PagesPaginationParams = Depends(),
        session: AsyncSession = Depends(get_async_session)
):
    university = await UniversityManager.get_all(
        limit=pagination.limit,
        offset=pagination.offset,
        session=session
    )

    return university

@router.post('/')
async def create_university():
    pass
