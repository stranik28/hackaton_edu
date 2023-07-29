from db.repository.base import BaseRepository
from db.models.address import Address
from sqlalchemy import select

from api.response.address import ResponseAddress
from api.request.address import RequestAddress


class AddressRepository(BaseRepository):

    async def get_all(
            self,
            limit: int,
            offset: int
    ) -> list[Address]:
        query = (
            select(Address)
            .limit(limit)
            .offset(offset)
        )
        return await self.all_ones(query=query)

    async def create(
            self,
            address: RequestAddress
    ) -> None:
        address_create = Address(**address.__dict__)
        await self.add_model(model=address_create)
