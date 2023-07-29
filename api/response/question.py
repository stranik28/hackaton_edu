from api.response.base import BaseModel
from pydantic import Field
from typing import Optional
from db.models.question import Question


class ResponseQuestion(BaseModel):
    id: int = Field(..., examples=[1])
    name: Optional[str] = Field(None, examples=['Вопрос про обед'])
    body: str = Field(..., examples=['Что будет в обед'])
    answer: list[int] = Field(..., examples=[[1, 2, 3]])
    type: int = Field(..., examples=[1])


class ResponseQuestionFactory:

    @classmethod
    def get_from_models(cls,
                              models: list[Question]) -> list[ResponseQuestion]:
        return [cls.get_from_model(model=model) for model in models]

    @staticmethod
    def get_from_model(
            model: Question
    ) -> ResponseQuestion:
        return ResponseQuestion(
            id=model.id,
            name=model.name,
            body=model.body,
            answer=model.answer,
            type=model.type
        )
