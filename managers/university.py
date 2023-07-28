from sqlalchemy.ext.asyncio import AsyncSession

from db.repository.university import UniversityRepository
from db.models.university import University

from api.request.university import RequestUniversity


class UniversityManager:

    @staticmethod
    async def get_all(
            session: AsyncSession,
            limit: int,
            offset: int
    ) -> list[University]:
        return await UniversityRepository(session).get_all(
            limit=limit,
            offset=offset
        )

    @staticmethod
    async def create(
            university: RequestUniversity,
            session: AsyncSession
    ) -> None:
        await UniversityRepository(session).create(
            university=university
        )
