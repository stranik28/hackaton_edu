from api.request.base import RequestBase
from pydantic import Field


class RequestExam(RequestBase):
    name: str = Field(..., examples=['математика профиль'])
