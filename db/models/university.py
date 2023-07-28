from database import Base
from sqlalchemy import Column, Integer, String, ARRAY, ForeignKey


class University(Base):
    __tablename__ = "university"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    photos = Column(ARRAY(String), nullable=True)
    address = Column(ARRAY(Integer), nullable=False)
    speciality = Column(ARRAY(Integer), nullable=False)
