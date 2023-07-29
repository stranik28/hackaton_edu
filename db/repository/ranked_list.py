from db.repository.base import BaseRepository
from db.models.ranked_list import RankedList
from sqlalchemy import select

from api.response.rankedlist import ResponseRankedList
from api.request.rankedlist import RequestRankedList


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
            rankedlist: RequestRankedList
    ) -> None:
        rankedlist_create = RankedList(**rankedlist.__dict__)
        await self.add_model(model=rankedlist_create)
        