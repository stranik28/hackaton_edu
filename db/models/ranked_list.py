from database import Base
from sqlalchemy import Column, Integer, ForeignKey, String


class RankedList(Base):
    __tablename__ = "ranked_list"
    id = Column(Integer, index=True, primary_key=True, nullable=False)
    speciality = Column(Integer, ForeignKey("speciality.id"), nullable=False)
    user = Column(Integer, ForeignKey("user.id"), nullable=False)
