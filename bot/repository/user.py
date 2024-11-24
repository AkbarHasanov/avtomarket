from bot.models.user import User
from bot.database.session import db


def create_user(user: User):
    db.add(user)
    db.commit()
    db.refresh(user)


def set_language(user: User, language: str):
    user.language = language
    db.commit()
    db.refresh(user)


def get_user_by_chat_id(chat_id: int):
    db.commit()
    return db.query(User).filter(User.chat_id == chat_id).first()


def get(user_id: int) -> User:
    db.commit()
    return db.query(User).filter(User.id == user_id).first()
