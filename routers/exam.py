from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from api.depends.pagination import PagesPaginationParams
from api.response.exam import ResponseExam
from api.response.exam import ResponseExamFactory
from api.request.exam import RequestExam
from api.response.base import ResponseEmpty

from db.models.exam import Exam

from database import get_async_session

from managers.exam import ExamManager

router = APIRouter(prefix='/exam', tags=['Exam'])


@router.get('/tech', response_model=list[ResponseExam])
async def all_exam(
        pagination: PagesPaginationParams = Depends(),
        session: AsyncSession = Depends(get_async_session)
):
    exams: list[Exam] = await ExamManager.get_all(
        limit=pagination.limit,
        offset=pagination.offset,
        session=session
    )
    return ResponseExamFactory.from_models(exams=exams)


@router.post('/', response_model=ResponseEmpty)
async def create_exam(
        request: RequestExam,
        session: AsyncSession = Depends(get_async_session)
):
    await ExamManager.create(
        exam=request,
        session=session
    )

    return ResponseEmpty()
