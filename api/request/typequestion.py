from api.request.base import RequestBase
from pydantic import Field


class TypeQuestion(RequestBase):
    name: str = Field(..., examples=["Одиночный выбор"])
