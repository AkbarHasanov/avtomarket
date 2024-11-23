from functools import partial
import config
from bot.repository.user import *
from config import *


def handle_question(bot, callback):
    user = get_user_by_chat_id(callback.message.chat.id)

    text = {
        UZBEK_LANGUAGE: """Iltimos, xabaringizni qoldiring va biz 24 soat ichida siz bilan bog'lanamiz.

Agar 24 soat ichida javob kelmasa, @avtomaruzb administratoriga murojaat qiling.""",
        RUSSIAN_LANGUAGE: """Пожалуйста оставьте свое сообщение и в тчении 24 часов мы свяжемся с вами.

Если в течении 24 часов вы не получите ответ, пожалуйста свяжитесь с администратором @avtomaruzb."""
    }

    event_help = bot.send_message(callback.message.chat.id, text=text[user.language])
    bot.register_next_step_handler(event_help, partial(send_question, bot=bot))


def send_question(message, bot):
    user = get_user_by_chat_id(message.chat.id)

    text = {
        UZBEK_LANGUAGE: f"""{message.text}\n\nFoydalanuvchi nomi: @{message.from_user.username}""",
        RUSSIAN_LANGUAGE: f"""{message.text}\n\nИмя пользователя: @{message.from_user.username}""",
    }
    bot.send_message(config.ADMIN_CHAT_ID, text=text[user.language])

    text = {
        UZBEK_LANGUAGE: "Xabar yuborildi, administrator tez orada siz bilan bog'lanadi.",
        RUSSIAN_LANGUAGE: "Сообщение было отправлено с вами скоро свяжеться администратор."
    }
    bot.send_message(message.chat.id, text=text[user.language])
