from api.response.base import ResponseBase
from pydantic import Field
from typing import Optional, List, Any, Coroutine
from db.models.speciality import Speciality


class ResponseSpecialityTech(ResponseBase):
    id: int = Field(..., examples=[1])
    name: str = Field(..., examples=['Геология'])
    code: str = Field(..., examples=['05.03.01'])
    description: Optional[str] = Field(None, examples=['Самая лучшая специальность. Можно копать землю. Или не копать.'])
    test: Optional[list[int]] = Field(None, examples=[1, 2, 3])
    exam: list[int] = Field(..., examples=[1, 2, 3])
    budget_place: int = Field(..., examples=[60])
    price: int = Field(..., examples=[140000])
    paid_place: int = Field(..., examples=[100])


class ResponseSpecialityTechFactory:

    @staticmethod
    def from_model(speciality: Speciality) -> ResponseSpecialityTech:
        return ResponseSpecialityTech(
            id=speciality.id,
            name=speciality.name,
            code=speciality.code,
            description=speciality.description,
            test=speciality.test,
            exam=speciality.exam,
            budget_place=speciality.budget_place,
            price=speciality.price,
            paid_place=speciality.paid_place
        )

    @classmethod
    def from_models(cls, specialities: list[Speciality]) -> list[ResponseSpecialityTech]:
        return [cls.from_model(speciality=speciality) for speciality in specialities]
