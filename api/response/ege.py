from api.response.base import ResponseBase
from pydantic import Field
from typing import Optional
from db.models.ege import Ege


class ResponseEge(ResponseBase):
    id: int = Field(..., examples=[1])
    exam: int = Field(..., examples=[1])
    score: Optional[int] = Field(None, examples=[100])


class ResponseEgeFactory:
    @staticmethod
    def from_model(ege: Ege) -> ResponseEge:
        return ResponseEge(
            id=ege.id,
            exam=ege.exam,
            score=ege.score
        )

    @classmethod
    def from_models(cls, eges: list[Ege]) -> list[ResponseEge]:
        return [cls.from_model(ege=ege) for ege in eges]
