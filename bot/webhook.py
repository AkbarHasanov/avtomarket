from flask import Flask, request
from telebot import types
from config import WEBHOOK_PATH
from bot.database.session import SessionLocal
from bot.bot import bot

app = Flask(__name__)


@app.route(WEBHOOK_PATH, methods=['POST'])
def webhook():
    """
    Telegram sends updates to this endpoint. The bot processes the updates.
    """
    json_data = request.get_json()
    if json_data:
        update = types.Update.de_json(json_data)
        bot.process_new_updates([update])
    return "", 200


@app.teardown_appcontext
def shutdown_session(exception=None):
    """
    Ensures the database session is closed after each request.
    """
    db = SessionLocal()
    db.remove()
