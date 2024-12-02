from bot.models.user import User
from bot.database.session import get_db


def create_user(user: User):
    db = get_db()
    db.add(user)
    db.commit()
    db.refresh(user)


def set_language(user: User, language: str):
    db = get_db()
    db.query(User).filter(User.id == user.id).update({"language": language})
    db.commit()


def get_user_by_chat_id(chat_id: int)->User:
    db = get_db()
    db.commit()
    return db.query(User).filter(User.chat_id == chat_id).first()


def get(user_id: int) -> User:
    db = get_db()
    db.commit()
    return db.query(User).filter(User.id == user_id).first()
