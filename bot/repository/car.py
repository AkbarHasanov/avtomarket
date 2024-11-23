from bot.database.session import db
from bot.models.car import Car, CarPhoto


def create_car(car: Car):
    db.add(car)
    db.commit()
    db.refresh(car)


def update_tariff(car: Car, tariff: str):
    car.tariff_id = tariff
    db.commit()
    db.refresh(car)


def get_last_car_by_user_id(user_id: str) -> Car:
    return db.query(Car).filter(Car.user_id == user_id).order_by(Car.created_at.desc()).one_or_none()


def add_car_photo(car_id, photo_path: str):
    photo = CarPhoto(car_id=car_id, path=photo_path)
    db.add(photo)
    db.commit()
    db.refresh(photo)


def get_photo_count(car_id: int) -> int:
    return db.query(CarPhoto).filter(CarPhoto.car_id == car_id).count()
