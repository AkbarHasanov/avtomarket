from telebot import TeleBot
from config import BOT_TOKEN
from bot.handlers import command_handler, callback_handler, photo_handler
from bot.database.session import engine
from bot.models.base import Base
from bot.repository.tariff import get_tariffs, init_tariffs

# Initialize bot
bot = TeleBot(BOT_TOKEN)

# Register Handlers
# message_handler.register_message_handlers(bot)
command_handler.register_command_handlers(bot)
callback_handler.register_callback_handlers(bot)
photo_handler.register_photo_handlers(bot)

# Initialize Database
Base.metadata.create_all(bind=engine)

if not get_tariffs():
    init_tariffs()

# Start polling
if __name__ == "__main__":
    print("Bot is running...")
    bot.polling(none_stop=True)
