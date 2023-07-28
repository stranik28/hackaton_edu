from database import Base
from sqlalchemy import Column, Integer, String, ARRAY, ForeignKey


class Question(Base):
    __tablename__ = "question"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, nullable=True)
    body = Column(String, nullable=False)
    answer = Column(ARRAY(Integer), nullable=False)
    type = Column(Integer, ForeignKey("type_question.id"), nullable=False)
