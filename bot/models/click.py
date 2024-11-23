from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship

from bot.models.base import Base
from datetime import datetime


class Click(Base):
    __tablename__ = "click_transactions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    click_trans_id = Column(String, unique=True, nullable=False)
    service_id = Column(String, nullable=False)
    click_paydoc_id = Column(Integer, nullable=False)
    merchant_trans_id = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    action = Column(Integer, nullable=False)
    error = Column(Integer, nullable=False)
    error_note = Column(String, nullable=False)
    sign_time = Column(String, nullable=False)
    sign_string = Column(String, nullable=False)
