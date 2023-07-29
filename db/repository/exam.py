from db.repository.base import BaseRepository
from db.models.exam import Exam
from sqlalchemy import select
from api.request.exam import RequestExam


class ExamRepository(BaseRepository):

    async def get_all(
            self,
            limit: int,
            offset: int
    ) -> list[Exam]:
        query = (
            select(Exam)
            .limit(limit)
            .offset(offset)
        )
        return await self.all_ones(query=query)

    async def create(
            self,
            exam: RequestExam
    ) -> None:
        exam_create = Exam(**exam.__dict__)
        await self.add_model(model=exam_create)
