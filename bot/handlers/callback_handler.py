from telebot import TeleBot
from const import *
from . import language_handler, question_handler, addvertisement_handler, tariff_handler


def register_callback_handlers(bot: TeleBot):
    @bot.callback_query_handler(func=lambda callback: callback.data)
    def check_callback_data(callback):
        if callback.data == CALLBACK_DATA_RU:
            language_handler.handle_russian(bot, callback)

        elif callback.data == CALLBACK_DATA_UZ:
            language_handler.handle_uzbek(bot, callback)

        elif callback.data == CALLBACK_DATA_GIVE_QUESTION:
            question_handler.handle_question(bot, callback)

        elif callback.data == CALLBACK_DATA_ADD_ADVERTISEMENT:
            addvertisement_handler.add_advertisement(bot, callback)

        elif callback.data == CALLBACK_DATA_ADD_PHOTOS:
            addvertisement_handler.add_photo(bot, callback)

        elif callback.data in [CALLBACK_DATA_ECONOMIC, CALLBACK_DATA_STANDARD, CALLBACK_DATA_PREMIUM,
                               CALLBACK_DATA_ELITE, CALLBACK_DATA_EXCLUSIVE, CALLBACK_DATA_EXTREME]:
            tariff_handler.choose_payment_system(bot, callback)

        elif callback.data == CALLBACK_DATA_CLICK:
            tariff_handler.click_payment(bot, callback)
