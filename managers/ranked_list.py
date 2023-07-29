from sqlalchemy.ext.asyncio import AsyncSession

from db.repository.ranked_list import RankedListRepository
from db.models.ranked_list import RankedList

from api.request.ranked_list import RequestRankedList


class RankedListManager:

    @staticmethod
    async def get_all(
            session: AsyncSession,
            limit: int,
            offset: int
    ) -> list[RankedList]:
        return await RankedListRepository(session).get_all(
            limit=limit,
            offset=offset
        )

    @staticmethod
    async def create(
            ranked_list: RequestRankedList,
            session: AsyncSession
    ) -> None:
        await RankedListRepository(session).create(
            ranked_list=ranked_list
        )
