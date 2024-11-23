from telebot import TeleBot
from bot.commands import start


def register_command_handlers(bot: TeleBot):
    @bot.message_handler(commands=['start'])
    def handle_start(message):
        start.start_command(bot, message)
