from api.request.base import RequestBase
from pydantic import Field


class RequestRankedList(RequestBase):
    speciality: int = Field(..., examples=[1])
    user: list[int] = Field(..., examples=[[1, 2, 3]])
