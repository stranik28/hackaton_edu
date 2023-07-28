from sqlalchemy import Column, Integer, String, ForeignKey, ARRAY
from database import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    username = Column(String, nullable=False)
    ege = Column(ARRAY(Integer), nullable=True)
    number_of_univers = Column(Integer, nullable=False)
    snils = Column(String, nullable=False)
