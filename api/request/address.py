from api.request.base import RequestBase
from pydantic import Field


class RequestAddress(RequestBase):
    region: str = Field(..., examples=["Краснодарский край"])
    city: str = Field(..., examples=["Краснодар"])
    street: str = Field(..., examples=["Ставропольская"])
    building: str = Field(..., examples=["149"])
    