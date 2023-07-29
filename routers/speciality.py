from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from api.depends.pagination import PagesPaginationParams
from api.response.speciality import ResponseSpecialityTech
from api.response.speciality import ResponseSpecialityTechFactory
from api.request.speciality import RequestSpeciality
from api.response.base import ResponseEmpty

from db.models.speciality import Speciality

from database import get_async_session

from managers.speciality import SpecialityManager

router = APIRouter(prefix='/speciality', tags=['Speciality'])


@router.get('/tech', response_model=list[ResponseSpecialityTech])
async def all_speciality(
        pagination: PagesPaginationParams = Depends(),
        session: AsyncSession = Depends(get_async_session)
):
    speciality: list[Speciality] = await SpecialityManager.get_all(
        limit=pagination.limit,
        offset=pagination.offset,
        session=session
    )
    return ResponseSpecialityTechFactory.from_models(specialities=speciality)


@router.post('/', response_model=ResponseEmpty)
async def create_speciality(
        request: RequestSpeciality,
        session: AsyncSession = Depends(get_async_session)
):
    await SpecialityManager.create(
        speciality=request,
        session=session
    )

    return ResponseEmpty()
