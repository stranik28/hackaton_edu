from api.response.base import ResponseBase
from pydantic import Field
from db.models.address import Address


class ResponseAddress(ResponseBase):
    id: int = Field(..., examples=[1])
    region: str = Field(..., examples=["Краснодарский край"])
    city: str = Field(..., examples=["Краснодар"])
    street: str = Field(..., examples=["Ставропольская"])
    building: str = Field(..., examples=["149"])


class ResponseAddressTech(ResponseBase):
    id: int = Field(..., examples=[1])
    region: str = Field(..., examples=["Краснодарский край"])
    city: str = Field(..., examples=["Краснодар"])
    street: str = Field(..., examples=["Ставропольская"])
    building: str = Field(..., examples=["149"])


class ResponseAddressTechFactory:
    @staticmethod
    def from_model(address: Address) -> ResponseAddressTech:
        return ResponseAddressTech(
            id=address.id,
            region=address.region,
            city=address.city,
            street=address.street,
            building=address.building,
        )

    @classmethod
    def from_models(cls, addresses: list[Address]) -> list[ResponseAddressTech]:
        return [cls.from_model(address=address) for address in addresses]
