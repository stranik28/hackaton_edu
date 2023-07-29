from db.repository.base import BaseRepository
from db.models.user import User
from sqlalchemy import select
from api.request.user import RequestUser


class UserRepository(BaseRepository):

    async def get_all(
            self,
            limit: int,
            offset: int
    ) -> list[User]:
        query = (
            select(User)
            .limit(limit)
            .offset(offset)
        )
        return await self.all_ones(query=query)

    async def create(
            self,
            user: RequestUser
    ) -> None:
        user_create = User(**user.__dict__)
        await self.add_model(model=user_create)
