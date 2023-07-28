from sqlalchemy.ext.asyncio import AsyncSession

from db.repository.university import UniversityRepository
from db.models.university import University


class UniversityManager:

    @staticmethod
    async def get_all(
            session: AsyncSession,
            limit: int,
            offset: int
    ) -> list[tuple[University, str]]:
        return await UniversityRepository(session).get_all(
            limit=limit,
            offset=offset
        )
