from api.response.base import ResponseBase
from pydantic import Field
from typing import Optional, List, Any, Coroutine
from db.models.user import User


class ResponseUser(ResponseBase):
    id: int = Field(..., examples=[1])
    username: str = Field(..., examples=['Nagibator2007'])
    ege: Optional[list[int]] = Field(None, examples=[[1, 2, 3]])
    number_of_univers: int = Field(..., examples=[3])
    snils: str = Field(..., examples=['228-128-69-42'])


class ResponseUserTechFactory:
    @staticmethod
    def from_model(user: User) -> ResponseUser:
        return ResponseUser(
            id=user.id,
            username=user.username,
            ege=user.ege,
            number_of_univers=user.number_of_univers,
            snils=user.snils,
        )

    @classmethod
    def from_models(cls, users: list[User]) -> list[ResponseUser]:
        return [cls.from_model(user=user) for user in users]
