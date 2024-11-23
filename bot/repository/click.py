from bot.models.click import Click
from bot.database.session import db


def create(transaction: Click)->int:
    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return transaction.id


def get(transaction_id: int):
    return db.query(Click).filter(Click.id == transaction_id).first()
