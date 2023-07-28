from db.repository.base import BaseRepository
from db.models.university import University
from sqlalchemy import select
from api.response.university import ResponseUniversity
from api.request.university import RequestUniversity


class UniversityRepository(BaseRepository):

    async def get_all(
            self,
            limit: int,
            offset: int
    ) -> list[University]:
        query = (
            select(University)
            .limit(limit)
            .offset(offset)
        )
        return await self.all_ones(query=query)

    async def create(
            self,
            university: RequestUniversity
    ) -> None:
        university_create = University(**university.__dict__)
        await self.add_model(model=university_create)
