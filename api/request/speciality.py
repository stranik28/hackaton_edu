from api.request.base import RequestBase
from pydantic import Field
from typing import Optional


class RequestSpeciality(RequestBase):
    name: str = Field(..., examples=['Геология'])
    code: str = Field(..., examples=['05.03.01'])
    description: Optional[str] = Field(None, examples=['Самая лучшая специальность. Можно копать землю. Или не копать.'])
    test: Optional[list[int]] = Field(None, examples=[[1, 2, 3]])
    exam: list[int] = Field(..., examples=[[1, 2, 3]])
    budget_place: int = Field(..., examples=[60])
    price: int = Field(..., examples=[140000])
    paid_place: int = Field(..., examples=[100])
