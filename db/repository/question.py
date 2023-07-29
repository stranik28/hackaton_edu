from db.repository.base import BaseRepository
from api.request.question import RequestQuestion
from db.models.question import Question
from sqlalchemy import select


class QuestionRepository(BaseRepository):

    async def create(self,
                     model: RequestQuestion) -> None:
        answer_model = Question(**model.__dict__)
        await self.add_model(answer_model)

    async def get_all(self,
                      limit: int,
                      offset: int) -> list[Question]:
        query = (
            select(Question)
            .select_from(Question)
            .limit(limit)
            .offset(offset)
        )

        return await self.all_ones(query)
