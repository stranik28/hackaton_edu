from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class Answer(Base):
    __tablename__ = "answer"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    correct = Column(Boolean, nullable=False, default=False)
