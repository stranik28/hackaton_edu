from db.repository.base import BaseRepository
from sqlalchemy import select
from db.models.type_question import TypeQuestion as TypeQuestionModel
from api.request.typequestion import TypeQuestion


class TypeQuestionRepository(BaseRepository):

    async def create(self,
                     type_question_elem: TypeQuestion) -> None:
        model = TypeQuestionModel(**type_question_elem.__dict__)
        return await self.add_model(model)

    async def get_all(self,
                      limit: int,
                      offset: int) -> list[TypeQuestionModel]:
        query = (
            select(TypeQuestionModel)
            .select_from(TypeQuestionModel)
            .limit(limit)
            .offset(offset)
        )

        return await self.all_ones(query)
