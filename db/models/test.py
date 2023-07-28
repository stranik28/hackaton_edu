from database import Base
from sqlalchemy import Column, Integer, ARRAY, String, ForeignKey


class Test(Base):
    __tablename__ = "test"
    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, nullable=False)
