from config import *
from bot.database.session import engine
from bot.models.base import Base
from bot.repository.tariff import get_tariffs, init_tariffs
from api.app import create_app
from bot.bot import bot
import logging

app = create_app()

# Initialize Database
Base.metadata.create_all(bind=engine)

if not get_tariffs():
    init_tariffs()

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level to DEBUG to capture all logs
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger('telebot')  # Get the logger for the telebot library

# Start polling
if __name__ == "__main__":
    print("Setting up webhook...")
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK_URL)

    # bot.infinity_polling()

    print(f"Webhook set at: {WEBHOOK_URL}")
    print("Starting Flask server...")
    app.run(host=HOST, port=PORT)
