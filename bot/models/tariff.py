from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from bot.models.base import Base


class Tariff(Base):
    __tablename__ = 'tariffs'

    id = Column(Integer, primary_key=True)
    amount = Column(Integer)

    cars = relationship('Car', back_populates='tariff')
    translations = relationship('Translation', back_populates='tariff')


class Translation(Base):
    __tablename__ = 'translations'

    id = Column(Integer, primary_key=True)
    tariff_id = Column(Integer, ForeignKey('tariffs.id'))
    name = Column(String)
    title = Column(String)
    description = Column(String)
    language = Column(String)
    label = Column(String)
    callback_data = Column(String)

    tariff = relationship('Tariff', back_populates='translations')
