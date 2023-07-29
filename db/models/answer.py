from database import Base
from sqlalchemy import Column, Integer, String, Boolean


class Answer(Base):
    __tablename__ = "answer"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    body = Column(String, nullable=False)
    correct = Column(Boolean, nullable=False, default=False)
