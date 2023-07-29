from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from api.depends.pagination import PagesPaginationParams
from api.request.question import RequestQuestion
from api.response.base import ResponseEmpty
from api.response.question import ResponseQuestion, ResponseQuestionFactory
from database import get_async_session
from managers.question import QuestionManager
from db.models.question import Question

router = APIRouter(prefix='/question', tags=['Question'])


@router.post('/', response_model=ResponseEmpty)
async def create(
        question: RequestQuestion,
        session: AsyncSession = Depends(get_async_session)
):
    await QuestionManager.create(model=question, session=session)
    return ResponseEmpty()


@router.get('/', response_model=list[ResponseQuestion])
async def get_all(
        pagination: PagesPaginationParams = Depends(),
        session: AsyncSession = Depends(get_async_session)
):
    questions: list[Question] = await QuestionManager.get_all(limit=pagination.limit, offset=pagination.offset,
                                                              session=session)
    return ResponseQuestionFactory.get_from_models(questions)