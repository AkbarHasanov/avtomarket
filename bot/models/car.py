import enum

from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Enum
from sqlalchemy.orm import relationship
from bot.models.base import Base
import datetime


# Define an Enum for status
class PaymentStatus(enum.Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress" 
    PAID = "paid"


class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    model = Column(String)
    price = Column(String)
    body_type = Column(String)
    mileage = Column(String)
    gearbox_type = Column(String)
    issue_year = Column(String)
    color = Column(String)
    engine_capacity = Column(String)
    fuel_type = Column(String)
    machine_condition = Column(String)
    number_of_owners = Column(String)
    city = Column(String)
    payment_type = Column(String)
    additional_options = Column(String)
    phone_number = Column(String)
    tariff_id = Column(String, ForeignKey('tariffs.id'), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.now())
    payment_status = Column(Enum(PaymentStatus), nullable=False, default=PaymentStatus.PENDING)

    owner = relationship('User', back_populates="cars")
    photos = relationship('CarPhoto', back_populates='car')
    tariff = relationship('Tariff', back_populates='cars')


class CarPhoto(Base):
    __tablename__ = 'car_photos'
    id = Column(Integer, autoincrement=True, primary_key=True)
    car_id = Column(Integer, ForeignKey('cars.id'), nullable=False)
    path = Column(String)

    car = relationship('Car', back_populates='photos')
