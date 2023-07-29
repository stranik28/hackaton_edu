from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from api.depends.pagination import PagesPaginationParams

from api.response.ranked_list import ResponseRankedList

from api.response.ranked_list import ResponseRankedListTechFactory
from api.request.ranked_list import RequestRankedList
from api.response.base import ResponseEmpty

from db.models.ranked_list import RankedList

from database import get_async_session

from managers.ranked_list import RankedListManager


router = APIRouter(prefix='/ranked_list', tags=['RankedList'])


@router.get('/tech', response_model=list[ResponseRankedList])
async def all_ranked_list(
        pagination: PagesPaginationParams = Depends(),
        session: AsyncSession = Depends(get_async_session)
):
    ranked_list: list[RankedList] = await RankedListManager.get_all(
        limit=pagination.limit,
        offset=pagination.offset,
        session=session
    )
    return ResponseRankedListTechFactory.from_models(ranked_lists=ranked_list)


@router.post('/', response_model=ResponseEmpty)
async def create_ranked_list(
        request: RequestRankedList,
        session: AsyncSession = Depends(get_async_session)
):
    await RankedListManager.create(
        ranked_list=request,
        session=session
    )

    return ResponseEmpty()
