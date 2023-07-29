from api.request.base import BaseModel
from pydantic import Field
from typing import Optional


class RequestQuestion(BaseModel):
    name: Optional[str] = Field(None, examples=['Вопрос про обед'])
    body: str = Field(..., examples=['Что будет в обед'])
    answer: list[int] = Field(..., examples=[[1, 2, 3]])
    type: int = Field(..., examples=[1])
