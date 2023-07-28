from sqlalchemy import Column, Integer, ForeignKey
from database import Base


class Ege(Base):
    __tablename__ = "ege"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    exam = Column(Integer, ForeignKey("exam.id"), nullable=False)
    score = Column(Integer, nullable=True)
