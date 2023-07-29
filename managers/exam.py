from sqlalchemy.ext.asyncio import AsyncSession

from db.repository.exam import ExamRepository
from db.models.exam import Exam

from api.request.exam import RequestExam


class ExamManager:

    @staticmethod
    async def get_all(
            session: AsyncSession,
            limit: int,
            offset: int
    ) -> list[Exam]:
        return await ExamRepository(session).get_all(
            limit=limit,
            offset=offset
        )

    @staticmethod
    async def create(
            exam: RequestExam,
            session: AsyncSession
    ) -> None:
        await ExamRepository(session).create(
            exam=exam
        )
