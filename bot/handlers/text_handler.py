from telebot import types, TeleBot
from addvertisement_handler import add_advertisement
from bot.commands.start import start_command
from functools import partial
from config import *


def register_text_handlers(bot: TeleBot):
    @bot.message_handler(content_types=['text'])
    def text_handler(message: types.Message):
        if message.text == "Сообщить о продаже машины 🚘":
            event_help = bot.send_message(message.chat.id, text="Пожалуйста оставьте отзыв о нашем канале 🙏🏻:")
            bot.register_next_step_handler(event_help, event_help_3)

        if message.text == "Avtomobil sotilgani haqida xabar bering 🚘":
            event_help = bot.send_message(message.chat.id, text="Kanalimiz haqida sharh qoldiring 🙏🏻:")
            bot.register_next_step_handler(event_help, partial(event_help_4, bot=bot))

        if message.text == "Дать рекламное обьявление 🛍" or message.text == "E'lon qo'ying 🛍":
            add_advertisement(bot, types.CallbackQuery(message=message))

        if message.text == "Нужна помощь с другим вопросом ❓":
            event_help = bot.send_message(message.chat.id,
                                          text="Пожалуйста оставьте свое сообщение и в тчении 24 часов мы свяжемся с вами."
                                               "Если в течении 24 часов вы не получите ответ, пожалуйста свяжитесь с администратором @avtomaruzb.")
            bot.register_next_step_handler(event_help, event_help_1)

        if message.text == "Boshqa savol bo'yicha yordam kerak ❓":
            event_help = bot.send_message(message.chat.id,
                                          text="Iltimos, xabaringizni qoldiring va biz 24 soat ichida siz bilan bog'lanamiz."
                                               "Agar 24 soat ichida javob kelmasa, @avtomaruzb administratoriga murojaat qiling.")
            bot.register_next_step_handler(event_help, event_help_2)


def event_help_3(message: types.Message, bot: TeleBot):
    bot.send_message(ADMIN_CHAT_ID,
                     text=f"Отзыв: {message.text} имя пользователя: @{message.from_user.username}")  # ------------------------------------------------------------------------------------------------------------------------------------
    markup = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id,
                     text="Благодарим вас за отзыв! Мы будем рады видеть вас снова и будем признательны, если вы порекомендуете наш канал другим 🙏🏻.",
                     reply_markup=markup)
    start_command(bot, message)


def event_help_4(message: types.Message, bot: TeleBot):
    bot.send_message(ADMIN_CHAT_ID,
                     text=f"Отзыв: {message.text} имя пользователя: @{message.from_user.username}")  # ------------------------------------------------------------------------------------------------------------------------------------
    markup = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id,
                     text="Fikr-mulohazangiz uchun rahmat! Sizni yana ko'rganimizdan xursand bo'lamiz va kanalimizni boshqalarga tavsiya qilsangiz minnatdor bo'lamiz 🙏🏻.",
                     reply_markup=markup)
    start_command(bot, message)


def event_help_1(message: types.Message, bot: TeleBot):
    bot.send_message(ADMIN_CHAT_ID,
                     text=f"{message.text} Имя пользователя: @{message.from_user.username}")  # ------------------------------------------------------------------------------------------------------------------------------------
    bot.send_message(message.chat.id, text="Сообщение было отправлено с вами скоро свяжеться администратор.")


def event_help_2(message: types.Message, bot: TeleBot):
    bot.send_message(ADMIN_CHAT_ID,
                     text=f"{message.text} Foydalanuvchi nomi: @{message.from_user.username}")  # ------------------------------------------------------------------------------------------------------------------------------------
    bot.send_message(message.chat.id, text="Xabar yuborildi, administrator tez orada siz bilan bog'lanadi.")
