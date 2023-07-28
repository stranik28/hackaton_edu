from typing import Any, Union, Tuple, Sequence

from sqlalchemy import select, exists, Result, Row
from sqlalchemy.engine import ChunkedIteratorResult
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import Select, Delete



class BaseRepository:
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def execute(self, query: Select) -> Result[Any]:
        return await self._session.execute(query)

    async def execute_parametrize(self, query: Union[str, Select], params: dict) -> Result[Any]:
        return await self._session.execute(statement=query, params=params)

    async def execute_fetch(self, query: Delete) -> Result[Any]:
        return await self._session.execute(
            query, execution_options=immutabledict({"synchronize_session": "fetch"})
        )

    async def one(self, query: Select) -> Any:
        result = await self.execute(query)
        return result.one()

    async def one_or_none(self, query: Select) -> Any:
        result = await self.execute(query)
        return result.one_or_none()

    async def one_val(self, query: Select) -> Any:
        result = await self.one(query)
        return result[0]

    async def one_or_none_val(self, query: Select) -> Any:
        result = await self.one_or_none(query)
        if not result:
            return None
        return result[0]

    async def add_model(self, model) -> None:
        self._session.add(model)
        await self._session.flush([model])

    async def add_model_ignore_exceptions(self, model) -> None:
        try:
            async with self._session.begin_nested():
                await self.add_model(model)
        except IntegrityError:
            pass

    async def add_models(self, models) -> None:
        for model in models:
            await self.add_model(model)

    async def delete(self, model) -> None:
        await self._session.delete(model)

    async def delete_many(self, models) -> None:
        for model in models:
            await self.delete(model)

    async def all(self, query: Select):
        result = await self.execute(query)
        return result.all()

    async def all_ones(self, query: Select) -> list[Any]:
        result = await self.execute(query)
        return [row[0] for row in result.all()]

    async def exists(self, query: Select) -> bool:
        query = select(exists(query))
        return await self.one_val(query)
