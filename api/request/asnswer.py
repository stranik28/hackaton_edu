from api.request.base import RequestBase
from pydantic import Field
from db.models.answer import Answer


class RequestAnswer(RequestBase):
    body: str = Field(..., examples=["Один"])
    correct: bool = Field(False, examples=[True])


