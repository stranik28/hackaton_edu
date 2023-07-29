from sqlalchemy.ext.asyncio import AsyncSession

from db.repository.answer import AnswerRepository
from db.models.answer import Answer as AnswerModel
from api.request.asnswer import RequestAnswer


class AnswerManager:

    @staticmethod
    async def create(
            model: RequestAnswer,
            session: AsyncSession
    ) -> None:
        await AnswerRepository(session).create(model=model)

    @staticmethod
    async def get_all(
            limit: int,
            offset: int,
            session: AsyncSession
    ) -> list[AnswerModel]:
        return await AnswerRepository(session).get_all(limit=limit, offset=offset)
