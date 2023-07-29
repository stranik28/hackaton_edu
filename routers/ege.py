from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from api.depends.pagination import PagesPaginationParams
from api.response.ege import ResponseEge
from api.response.ege import ResponseEgeFactory
from api.request.ege import RequestEge
from api.response.base import ResponseEmpty

from db.models.ege import Ege

from database import get_async_session

from managers.ege import EgeManager

router = APIRouter(prefix='/ege', tags=['Ege'])


@router.get('/tech', response_model=list[ResponseEge])
async def all_ege(
        pagination: PagesPaginationParams = Depends(),
        session: AsyncSession = Depends(get_async_session)
):
    eges: list[Ege] = await EgeManager.get_all(
        limit=pagination.limit,
        offset=pagination.offset,
        session=session
    )
    return ResponseEgeFactory.from_models(eges=eges)


@router.post('/', response_model=ResponseEmpty)
async def create_ege(
        request: RequestEge,
        session: AsyncSession = Depends(get_async_session)
):
    await EgeManager.create(
        ege=request,
        session=session
    )

    return ResponseEmpty()
