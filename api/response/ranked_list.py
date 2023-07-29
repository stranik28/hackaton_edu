from api.request.base import RequestBase
from pydantic import Field


class ResponseRankedList(RequestBase):
    id: int = Field(..., examples=[1])
    speciality: int = Field(..., examples=[1])
    user: list[int] = Field(..., examples=[[1, 2, 3]])
