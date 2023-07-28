from database import Base
from sqlalchemy import Column, Integer, String


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    region = Column(String, index=True, unique=True, nullable=False)
    city = Column(String, index=True, nullable=False)
    street = Column(String, nullable=False)
    building = Column(String, nullable=False)
