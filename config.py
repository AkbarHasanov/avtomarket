from dotenv import load_dotenv
import os

load_dotenv()


HOST=os.getenv("HOST")
PORT=os.getenv("PORT")


DATABASE_URL = os.getenv("DATABASE_URL")

WEBHOOK_URL=os.getenv("WEBHOOK_URL")
WEBHOOK_PATH=os.getenv("WEBHOOK_PATH")
print(WEBHOOK_PATH, WEBHOOK_URL)
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_PAY_TOKEN = os.getenv('BOT_PAY_TOKEN')
ADMIN_CHAT_ID = os.getenv('ADMIN_CHAT_ID')

CLICK_SERVICE_ID = os.getenv('CLICK_SERVICE_ID')
CLICK_MERCHANT_ID = os.getenv('CLICK_MERCHANT_ID')
CLICK_SECRET_KEY = os.getenv('CLICK_SECRET_KEY')

PAYME_URI = os.getenv('PAYME_URI')
PAYME_MERCHANT_ID = os.getenv('PAYME_MERCHANT_ID')
PAYME_KEY = os.getenv('PAYME_KEY', '')

RETURN_URL = os.getenv('RETURN_URL')

UZBEK_LANGUAGE = "UZ"
RUSSIAN_LANGUAGE = "RU"