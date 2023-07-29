from fastapi import APIRouter, Depends
from api.response.base import ResponseEmpty
from api.request.typequestion import TypeQuestion
from managers.type_question import ManagerTypeQuestion
from database import get_async_session
from api.response.type_question import ResponseTypeQuestion
from api.depends.pagination import PagesPaginationParams
from api.response.type_question import ResponseTypeQuestionFactory

from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/type_question", tags=["TypeQuestion"])


@router.post("/", response_model=ResponseEmpty)
async def create(
        type_question_elem: TypeQuestion = Depends(),
        session: AsyncSession = Depends(get_async_session)
):
    await ManagerTypeQuestion.create(session=session, type=type_question_elem)
    return ResponseEmpty()


@router.get("/", response_model=list[ResponseTypeQuestion])
async def get_all(
        pagination: PagesPaginationParams = Depends(),
        session: AsyncSession = Depends(get_async_session)

):
    datas = await ManagerTypeQuestion.get_all(limit=pagination.limit, offset=pagination.offset, session=session)

    return ResponseTypeQuestionFactory.get_from_models(datas)
