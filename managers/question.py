from sqlalchemy.ext.asyncio import AsyncSession

from api.request.question import RequestQuestion
from db.models.question import Question
from db.repository.question import QuestionRepository


class QuestionManager:

    @staticmethod
    async def get_all(
            session: AsyncSession,
            limit: int,
            offset: int
    ) -> list[Question]:
        return await QuestionRepository(session).get_all(limit=limit, offset=offset)

    @staticmethod
    async def create(
            session: AsyncSession,
            model: RequestQuestion
    ) -> None:
        await QuestionRepository(session).create(model=model)
