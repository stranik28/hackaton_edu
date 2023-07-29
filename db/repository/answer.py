from db.repository.base import BaseRepository
from api.request.asnswer import RequestAnswer
from db.models.answer import Answer as AnswerModel
from sqlalchemy import select


class AnswerRepository(BaseRepository):

    async def create(self,
                     model: RequestAnswer) -> None:
        answer_model: AnswerModel = AnswerModel(**model.__dict__)

        return await self.add_model(answer_model)

    async def get_all(self,
                      limit: int,
                      offset: int) -> list[AnswerModel]:
        query = (
            select(AnswerModel)
            .select_from(AnswerModel)
            .limit(limit)
            .offset(offset)
        )

        return await self.all_ones(query=query)
