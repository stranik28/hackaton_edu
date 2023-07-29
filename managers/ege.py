from sqlalchemy.ext.asyncio import AsyncSession

from db.repository.ege import EgeRepository
from db.models.ege import Ege

from api.request.ege import RequestEge


class EgeManager:

    @staticmethod
    async def get_all(
            session: AsyncSession,
            limit: int,
            offset: int
    ) -> list[Ege]:
        return await EgeRepository(session).get_all(
            limit=limit,
            offset=offset
        )

    @staticmethod
    async def create(
            ege: RequestEge,
            session: AsyncSession
    ) -> None:
        await EgeRepository(session).create(
            ege=ege
        )
