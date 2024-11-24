from telebot import TeleBot
from config import *
from bot.handlers import command_handler, callback_handler, photo_handler

# Initialize bot
bot = TeleBot(BOT_TOKEN)

# Register Handlers
command_handler.register_command_handlers(bot)
callback_handler.register_callback_handlers(bot)
photo_handler.register_photo_handlers(bot)
