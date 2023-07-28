from database import Base
from sqlalchemy import Column, String, Integer


class TypeQuestion(Base):
    __tablename__ = "type_question"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, nullable=False)
