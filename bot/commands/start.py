from telebot import types
import config
from bot.repository.user import *
from bot.const import *

def start_command(bot, message):
    user = get_user_by_chat_id(message.chat.id)

    if not user:
        user = User(
            chat_id=message.from_user.id,
            username=message.from_user.username
        )
        create_user(user)

    welcome_msg = """Avtomarket Uzbekistan xush kelibsiz!

Bu yerda siz hohlagan avtomobilingizni eng yaxshi narxlarda sotishingiz va xarid qilishingiz, shuningdek, bozordagi joriy narxlar bilan tanishishingiz mumkin.

-----------------------------------------

Добро пожаловать на Avtomarket Uzbekistan!

Тут вы можете продать и купить любую вами желаемую машину по самым выгодным ценам, а так же ознакомиться с актуальными ценами на рынке."""
    bot.send_message(message.chat.id, welcome_msg)

    text = f'Клиент запустил бот\n\nЮзернейм: @{message.from_user.username}'
    bot.send_message(config.ADMIN_CHAT_ID, text=text)


    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(
        "🇺🇿O'zbekcha", callback_data=CALLBACK_DATA_UZ))
    markup.add(types.InlineKeyboardButton(
        "🇷🇺Русский", callback_data=CALLBACK_DATA_RU))

    text = 'Kerakli tilni tanlang.\n\nВыберите желаемый язык.'
    bot.send_message(message.chat.id, text=text, reply_markup=markup)
