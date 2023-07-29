from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from api.depends.pagination import PagesPaginationParams

from api.response.address import ResponseAddress
from api.response.address import ResponseAddressTech

from api.response.address import ResponseAddressTechFactory
from api.request.address import RequestAddress
from api.response.base import ResponseEmpty

from db.models.address import Address

from database import get_async_session

from managers.address import AddressManager


router = APIRouter(prefix='/address', tags=['Address'])


@router.get('/tech', response_model=list[ResponseAddressTech])
async def all_address(
        pagination: PagesPaginationParams = Depends(),
        session: AsyncSession = Depends(get_async_session)
):
    address: list[Address] = await AddressManager.get_all(
        limit=pagination.limit,
        offset=pagination.offset,
        session=session
    )
    return ResponseAddressTechFactory.from_models(addresses=address)


@router.post('/', response_model=ResponseEmpty)
async def create_address(
        request: RequestAddress,
        session: AsyncSession = Depends(get_async_session)
):
    await AddressManager.create(
        address=request,
        session=session
    )

    return ResponseEmpty()
