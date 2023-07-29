from sqlalchemy.ext.asyncio import AsyncSession
from api.request.typequestion import TypeQuestion
from db.repository.type_question import TypeQuestionRepository
from db.models.type_question import TypeQuestion


class ManagerTypeQuestion:

    @staticmethod
    async def create(
            type: TypeQuestion,
            session: AsyncSession
    ) -> None:
        return await TypeQuestionRepository(session).create(type_question_elem=type)

    @staticmethod
    async def get_all(
            session: AsyncSession,
            limit: int,
            offset: int
    ) -> list[TypeQuestion]:
        return await TypeQuestionRepository(session).get_all(limit=limit, offset=offset)
