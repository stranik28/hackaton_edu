from api.request.base import RequestBase
from pydantic import Field
from typing import Optional


class RequestUser(RequestBase):
    username: str = Field(..., examples=['Nagibator2007']),
    ege: Optional[list[int]] = Field(None, examples=[[1, 2, 3]]),
    number_of_univers: int = Field(..., examples=[3])
    snils: str = Field(..., examples=['228-128-69-42'])
