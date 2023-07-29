from db.repository.base import BaseRepository
from db.models.speciality import Speciality
from sqlalchemy import select
from api.response.speciality import ResponseSpecialityTech
from api.request.speciality import RequestSpeciality


class SpecialityRepository(BaseRepository):

    async def get_all(
            self,
            limit: int,
            offset: int
    ) -> list[Speciality]:
        query = (
            select(Speciality)
            .limit(limit)
            .offset(offset)
        )
        return await self.all_ones(query=query)

    async def create(
            self,
            speciality: RequestSpeciality
    ) -> None:
        speciality_create = Speciality(**speciality.__dict__)
        await self.add_model(model=speciality_create)
