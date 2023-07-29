from sqlalchemy.ext.asyncio import AsyncSession

from db.repository.address import AddressRepository
from db.models.address import Address

from api.request.address import RequestAddress


class AddressManager:

    @staticmethod
    async def get_all(
            session: AsyncSession,
            limit: int,
            offset: int
    ) -> list[Address]:
        return await AddressRepository(session).get_all(
            limit=limit,
            offset=offset
        )

    @staticmethod
    async def create(
            address: RequestAddress,
            session: AsyncSession
    ) -> None:
        await AddressRepository(session).create(
            address=address
        )
