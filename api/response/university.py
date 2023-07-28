from api.response.base import ResponseBase
from pydantic import Field


class ResponseUniversity(ResponseBase):
    id: int = Field(..., examples=[1])
    name: str = Field(..., examples=['Кубанский государственный университет'])
    city: str = Field(..., examples=['Краснодар'])
    picture: str = Field(..., examples=["https://shorturl.at/oquL9"])
