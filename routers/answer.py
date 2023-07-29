from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from api.response.base import ResponseEmpty
from managers.answer import AnswerManager
from db.models.answer import Answer as AnswerModel

from api.request.asnswer import RequestAnswer
from api.response.answer import ResponseAnswer, ResponseAnswerFactory

from api.depends.pagination import PagesPaginationParams

from database import get_async_session

router = APIRouter(prefix="/answer", tags=["Answer"])


@router.get("/", response_model=list[ResponseAnswer])
async def get_all(
        pagination: PagesPaginationParams = Depends(),
        session: AsyncSession = Depends(get_async_session)
):
    answers: list[AnswerModel] = await AnswerManager.get_all(limit=pagination.limit,
                                                             offset=pagination.offset,
                                                             session=session)
    return ResponseAnswerFactory.get_from_models(answers)


@router.post("/", response_model=ResponseEmpty)
async def create(
        answer: RequestAnswer,
        session: AsyncSession = Depends(get_async_session)
):
    await AnswerManager.create(model=answer, session=session)
    return ResponseEmpty()
