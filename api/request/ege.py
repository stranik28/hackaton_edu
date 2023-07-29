from api.request.base import RequestBase
from pydantic import Field
from typing import Optional


class RequestEge(RequestBase):
    exam: int = Field(..., examples=[1]),
    score: Optional[int] = Field(None, examples=[100])
