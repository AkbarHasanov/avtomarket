from sqlalchemy import Column, Integer, String, Float, DateTime

from bot.models.base import Base
from datetime import datetime


class Payme(Base):
    __tablename__ = "payme_transactions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    amount = Column(Float, nullable=False)
    transaction_id = Column(String, nullable=False)
    created_at_payme = Column(Integer, nullable=False, default=int(datetime.now().timestamp()))
    order_id = Column(String, nullable=False)
    create_time = Column(Integer, nullable=False, default=int(datetime.now().timestamp()*1000))
    state = Column(Integer, nullable=False, default=0)
    perform_time = Column(Integer, nullable=True)
    cancel_time = Column(Integer, nullable=True)
    reason = Column(Integer, nullable=True)
