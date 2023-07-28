from db.repository.base import BaseRepository
from db.models.university import University
from sqlalchemy import select
from db.models.address import Address


class UniversityRepository(BaseRepository):

    async def get_all(
            self,
            limit: int,
            offset: int
    ) -> list[tuple[University, str]]:
        query_1 = (
            select(University, Address.city)
            .select_from(University)
            .join(Address, Address.id == University.address[0], isouter=False)
            .limit(limit)
            .offset(offset)
            .distinct()
        )

        return await self.all(query_1)
