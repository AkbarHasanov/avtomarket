from datetime import datetime

from bot.models.payme import Payme
from bot.database.session import get_db


def create(transaction: Payme) -> Payme:
    db = get_db()
    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return transaction


def get(transaction_id: int):
    db = get_db()
    return db.query(Payme).filter(Payme.id == transaction_id).first()


def get_by_transaction_id(transaction_id: int):
    db = get_db()
    return db.query(Payme).filter(Payme.transaction_id == transaction_id).first()


def perform(transaction_id: int) -> Payme:
    db = get_db()
    db.query(Payme).filter(Payme.transaction_id == transaction_id).update(
        {"state": 2, "perform_time": int(datetime.now().timestamp()*1000)})

    db.commit()
    return get_by_transaction_id(transaction_id)


def cancel(transaction_id: int, reason: int, state: int = -1):
    db = get_db()
    db.query(Payme).filter(Payme.transaction_id == transaction_id).update(
        {"state": state, "cancel_time": int(datetime.now().timestamp()*1000), "reason": reason})

    db.commit()
    return get_by_transaction_id(transaction_id)


def get_all(from_time: int, to_time: int):
    db = get_db()
    return db.query(Payme).filter(Payme.create_time >= from_time, Payme.create_time <= to_time).all()
