from sqlalchemy.ext.asyncio import AsyncSession

from db.repository.user import UserRepository
from db.models.user import User

from api.request.user import RequestUser


class UserManager:

    @staticmethod
    async def get_all(
            session: AsyncSession,
            limit: int,
            offset: int
    ) -> list[User]:
        return await UserRepository(session).get_all(
            limit=limit,
            offset=offset
        )

    @staticmethod
    async def create(
            user: RequestUser,
            session: AsyncSession
    ) -> None:
        await UserRepository(session).create(
            user=user
        )
