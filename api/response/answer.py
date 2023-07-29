from db.models.answer import Answer
from pydantic import Field
from api.response.base import ResponseBase


class ResponseAnswer(ResponseBase):
    id: int = Field(..., examples=[1, 2, 3])
    body: str = Field(..., examples=["Один"])
    correct: bool = Field(False, examples=[True])


class ResponseAnswerFactory:

    @classmethod
    def get_from_models(cls,
                        models: list[Answer]) -> list[ResponseAnswer]:
        return [cls.get_from_model(model) for model in models]

    @staticmethod
    def get_from_model(
            model: Answer) -> ResponseAnswer:
        return ResponseAnswer(
            id=model.id,
            body=model.body,
            correct=model.correct
        )
