from bot.database.session import get_db
from bot.models.car import Car, CarPhoto, PaymentStatus


def create_car(car: Car):
    db = get_db()
    db.add(car)
    db.commit()
    db.refresh(car)


def update_tariff(car: Car, tariff: str):
    db = get_db()
    db.query(Car).filter(Car.id == car.id).update({"tariff_id": tariff})
    db.commit()


def get_last_car_by_user_id(user_id: int) -> Car:
    db = get_db()
    return db.query(Car).filter(Car.user_id == user_id).order_by(Car.created_at.desc()).limit(1).one_or_none()


def get_car_by_id(car_id: int) -> Car:
    db = get_db()
    return db.query(Car).filter(Car.id == car_id).order_by(Car.created_at.desc()).limit(1).one_or_none()


def add_car_photo(car_id, photo_path: str):
    db = get_db()
    photo = CarPhoto(car_id=car_id, path=photo_path)
    db.add(photo)
    db.commit()


def get_photo_count(car_id: int) -> int:
    db = get_db()
    return db.query(CarPhoto).filter(CarPhoto.car_id == car_id).count()


def update_status(car: Car, status: PaymentStatus):
    db = get_db()
    db.query(Car).filter(Car.id == car.id).update({"status": status})
    db.commit()


def set_model(car_id: int, model: str):
    db = get_db()
    db.query(Car).filter(Car.id == car_id).update({"model": model})
    db.commit()


def set_price(car_id: int, price: str):
    db = get_db()
    db.query(Car).filter(Car.id == car_id).update({"price": price})
    db.commit()


def set_body_type(car_id: int, body_type: str):
    db = get_db()
    db.query(Car).filter(Car.id == car_id).update({"body_type": body_type})
    db.commit()


def set_mileage(car_id: int, mileage: str):
    db = get_db()
    db.query(Car).filter(Car.id == car_id).update({"mileage": mileage})
    db.commit()


def set_gearbox_type(car_id: int, gearbox_type: str):
    db = get_db()
    db.query(Car).filter(Car.id == car_id).update({"gearbox_type": gearbox_type})
    db.commit()


def set_issue_year(car_id: int, issue_year: str):
    db = get_db()
    db.query(Car).filter(Car.id == car_id).update({"issue_year": issue_year})
    db.commit()


def set_color(car_id: int, color: str):
    db = get_db()
    db.query(Car).filter(Car.id == car_id).update({"color": color})
    db.commit()


def set_engine_capacity(car_id: int, engine_capacity: str):
    db = get_db()
    db.query(Car).filter(Car.id == car_id).update({"engine_capacity": engine_capacity})
    db.commit()


def set_number_of_owners(car_id: int, number_of_owners: str):
    db = get_db()
    db.query(Car).filter(Car.id == car_id).update({"number_of_owners": number_of_owners})
    db.commit()


def set_phone_number(car_id: int, phone_number: str):
    db = get_db()
    db.query(Car).filter(Car.id == car_id).update({"phone_number": phone_number})
    db.commit()


def set_city(car_id: int, city: str):
    db = get_db()
    db.query(Car).filter(Car.id == car_id).update({"city": city})
    db.commit()


def set_payment_type(car_id: int, payment_type: str):
    db = get_db()
    db.query(Car).filter(Car.id == car_id).update({"payment_type": payment_type})
    db.commit()


def set_additional_options(car_id: int, additional_options: str):
    db = get_db()
    db.query(Car).filter(Car.id == car_id).update({"additional_options": additional_options})
    db.commit()


def set_fuel_type(car_id: int, fuel_type: str):
    db = get_db()
    db.query(Car).filter(Car.id == car_id).update({"fuel_type": fuel_type})
    db.commit()


def set_machine_condition(car_id: int, machine_condition: str):
    db = get_db()
    db.query(Car).filter(Car.id == car_id).update({"machine_condition": machine_condition})
    db.commit()
