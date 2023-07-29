from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from api.depends.pagination import PagesPaginationParams
from api.response.university import ResponseUniversityTech, ResponseUniversityTechFactory
from api.request.university import RequestUniversity
from api.response.base import ResponseEmpty

from db.models.university import University

from database import get_async_session

from managers.university import UniversityManager

router = APIRouter(prefix='/university', tags=['University'])


@router.get('/tech', response_model=list[ResponseUniversityTech])
async def all_university(
        pagination: PagesPaginationParams = Depends(),
        session: AsyncSession = Depends(get_async_session)
):
    university: list[University] = await UniversityManager.get_all(
        limit=pagination.limit,
        offset=pagination.offset,
        session=session
    )
    return ResponseUniversityTechFactory.from_models(university=university)


@router.post('/', response_model=ResponseEmpty)
async def create_university(
        request: RequestUniversity,
        session: AsyncSession = Depends(get_async_session)
):
    await UniversityManager.create(
        university=request,
        session=session
    )

    return ResponseEmpty()
