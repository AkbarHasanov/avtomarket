from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from bot.models.base import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    chat_id = Column(String, unique=True, nullable=False)
    language = Column(String, nullable=False, default="UZ")
    created_at = Column(DateTime, default=datetime.utcnow)

    cars = relationship("Car", back_populates="owner", cascade="all, delete-orphan")
