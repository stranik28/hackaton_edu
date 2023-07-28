from api.response.base import ResponseBase
from pydantic import Field
from typing import Optional, List, Any, Coroutine
from db.models.university import University


class ResponseUniversity(ResponseBase):
    id: int = Field(..., examples=[1])
    name: str = Field(..., examples=['Кубанский государственный университет'])
    city: str = Field(..., examples=['Краснодар'])
    picture: Optional[str] = Field(..., examples=["https://shorturl.at/oquL9"])


class ResponseUniversityTech(ResponseBase):
    id: int = Field(..., examples=[1])
    name: str = Field(..., examples=['Кубанский государственный университет'])
    photos: Optional[list[str]] = Field(None, examples=["https://shorturl.at/oquL9"])
    description: Optional[str] = Field(None, examples=['Описание'])
    address: Optional[list[int]] = Field(None, examples=[[1, 2, 3]])
    speciality: Optional[list[int]] = Field(None, examples=[[1, 2, 3]])


class ResponseUniversityTechFactory:

    @staticmethod
    def from_model(university: University) -> ResponseUniversityTech:
        return ResponseUniversityTech(
            id=university.id,
            name=university.name,
            photos=university.photos,
            description=university.description,
            address=university.address,
            speciality=university.speciality
        )

    @classmethod
    def from_models(cls, university: list[University]) -> list[ResponseUniversityTech]:
        return [cls.from_model(university=universit) for universit in university]
