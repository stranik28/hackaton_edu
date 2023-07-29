from api.request.base import RequestBase
from pydantic import Field
from db.models.ranked_list import RankedList


class ResponseRankedList(RequestBase):
    id: int = Field(..., examples=[1])
    speciality: int = Field(..., examples=[1])
    user: list[int] = Field(..., examples=[[1, 2, 3]])


class ResponseRankedListTechFactory:
    @staticmethod
    def from_model(ranked_list: RankedList) -> ResponseRankedList:
        return ResponseRankedList(
            id=ranked_list.id,
            speciality=ranked_list.speciality,
            user=ranked_list.user
        )

    @classmethod
    def from_models(cls, ranked_lists: list[RankedList]) -> list[ResponseRankedList]:
        return [cls.from_model(ranked_list=ranked_list) for ranked_list in ranked_lists]
