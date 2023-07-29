from sqlalchemy.ext.asyncio import AsyncSession

from db.repository.speciality import SpecialityRepository
from db.models.speciality import Speciality

from api.request.speciality import RequestSpeciality


class SpecialityManager:

    @staticmethod
    async def get_all(
            session: AsyncSession,
            limit: int,
            offset: int
    ) -> list[Speciality]:
        return await SpecialityRepository(session).get_all(
            limit=limit,
            offset=offset
        )

    @staticmethod
    async def create(
            speciality: RequestSpeciality,
            session: AsyncSession
    ) -> None:
        await SpecialityRepository(session).create(
            speciality=speciality
        )
