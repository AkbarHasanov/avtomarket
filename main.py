from config import *
from bot.database.session import engine
from bot.models.base import Base
from bot.repository.tariff import get_tariffs, init_tariffs
from api.app import create_app
from bot.bot import bot

app = create_app()

# Initialize Database
Base.metadata.create_all(bind=engine)

if not get_tariffs():
    init_tariffs()

# Start polling
if __name__ == "__main__":
    print("Setting up webhook...")
    bot.remove_webhook()
    # bot.set_webhook(url=WEBHOOK_URL)

    bot.infinity_polling()

    print(f"Webhook set at: {WEBHOOK_URL}")
    print("Starting Flask server...")
    app.run(host=HOST, port=PORT)
