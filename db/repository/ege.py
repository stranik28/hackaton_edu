from db.repository.base import BaseRepository
from db.models.ege import Ege
from sqlalchemy import select
from api.request.ege import RequestEge


class EgeRepository(BaseRepository):

    async def get_all(
            self,
            limit: int,
            offset: int
    ) -> list[Ege]:
        query = (
            select(Ege)
            .limit(limit)
            .offset(offset)
        )
        return await self.all_ones(query=query)

    async def create(
            self,
            ege: RequestEge
    ) -> None:
        ege_create = Ege(**ege.__dict__)
        await self.add_model(model=ege_create)
