from api.request.base import RequestBase
from pydantic import Field
from typing import Optional


class RequestUniversity(RequestBase):
    name: str = Field(..., examples=["Кубанский Государственный Университет"])
    photos: Optional[list[str]] = Field(..., examples=[["https://shorturl.at/ISUV5"]])
    description: Optional[str] = Field(..., examples=[
        "Кубанский государственный университет — один из крупнейших вузов России,"
        " расположенный в Краснодаре. Основан в 1920 году. Входит в состав"
        " Топ-1000 лучших университетов мира по версии университетского рейтинга"
        " Webometrics Ranking of World Universities."])
    address: Optional[list[int]] = Field(None, examples=[[1, 2, 3]])
    speciality: Optional[list[int]] = Field(None, examples=[[1, 2, 3]])
    phone: Optional[str] = Field(None, examples=["+7(999)999-99-99"])
