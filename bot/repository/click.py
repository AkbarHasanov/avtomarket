from bot.models.click import Click
from bot.database.session import get_db


def create(transaction: Click)->int:
    db = get_db()
    db.add(transaction)
    db.commit()
    db.refresh(transaction)

    return transaction.id


def get(transaction_id: int):
    db = get_db()
    return db.query(Click).filter(Click.id == transaction_id).first()
