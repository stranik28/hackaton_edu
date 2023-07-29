from api.response.base import BaseModel
from pydantic import Field
from db.models.type_question import TypeQuestion


class ResponseTypeQuestion(BaseModel):
    id: int = Field(..., examples=[1])
    name: str = Field(..., examples=['Одиночный выбор'])


class ResponseTypeQuestionFactory:

    @classmethod
    def get_from_models(cls, models: list[TypeQuestion]) -> list[ResponseTypeQuestion]:
        return [cls.get_from_model(model) for model in models]

    @staticmethod
    def get_from_model(
            model: TypeQuestion
    ) -> ResponseTypeQuestion:
        return ResponseTypeQuestion(
            id=model.id,
            name=model.name
        )
