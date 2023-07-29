from db.repository.base import BaseRepository
from db.models.ranked_list import RankedList
from sqlalchemy import select

from api.response.ranked_list import ResponseRankedList
from api.request.ranked_list import RequestRankedList


class RankedListRepository(BaseRepository):

    async def get_all(
            self,
            limit: int,
            offset: int
    ) -> list[RankedList]:
        query = (
            select(RankedList)
            .limit(limit)
            .offset(offset)
        )
        return await self.all_ones(query=query)

    async def create(
            self,
            ranked_list: RequestRankedList
    ) -> None:
        ranked_list_create = RankedList(**ranked_list.__dict__)
        await self.add_model(model=ranked_list_create)
        