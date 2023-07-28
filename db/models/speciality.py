from database import Base
from sqlalchemy import Column, Integer, String, ARRAY, ForeignKey


class Speciality(Base):
    __tablename__ = "speciality"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    code = Column(String, index=True, nullable=False)
    description = Column(String, nullable=False)
    test = Column(ARRAY(Integer), nullable=False)
    exam = Column(ARRAY(Integer), nullable=False)
    budget_place = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    paid_place = Column(Integer, nullable=False)
