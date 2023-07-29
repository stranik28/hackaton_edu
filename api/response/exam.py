from api.response.base import ResponseBase
from pydantic import Field
from typing import Optional
from db.models.exam import Exam


class ResponseExam(ResponseBase):
    id: int = Field(..., examples=[1])
    name: str = Field(..., examples=['Математика база'])


class ResponseExamFactory:
    @staticmethod
    def from_model(exam: Exam) -> ResponseExam:
        return ResponseExam(
            id=exam.id,
            name=exam.name,
        )

    @classmethod
    def from_models(cls, exams: list[Exam]) -> list[ResponseExam]:
        return [cls.from_model(exam=exam) for exam in exams]
