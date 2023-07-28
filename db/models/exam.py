from database import Base
from sqlalchemy import Column, Integer, String


class Exam(Base):
    __tablename__ = "exam"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String)
