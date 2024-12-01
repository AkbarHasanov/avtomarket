from telebot import TeleBot, types
from const import *
from . import language_handler, question_handler, addvertisement_handler, tariff_handler, payment_handler


def register_callback_handlers(bot: TeleBot):
    @bot.callback_query_handler(func=lambda callback: callback.data)
    def check_callback_data(callback: types.CallbackQuery):
        print(callback.data)
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
            payment_handler.click_payment(bot, callback)

        elif callback.data == CALLBACK_DATA_PAYME:
            payment_handler.payme_payment(bot, callback)

        elif callback.data in [CALLBACK_DATA_BODY_TYPE_SEDAN, CALLBACK_DATA_BODY_TYPE_COUPE,
                               CALLBACK_DATA_BODY_TYPE_HATCHBACK, CALLBACK_DATA_BODY_TYPE_UNIVERSAL,
                               CALLBACK_DATA_BODY_TYPE_CROSSOVER, CALLBACK_DATA_BODY_TYPE_SUV,
                               CALLBACK_DATA_BODY_TYPE_OTHER]:
            addvertisement_handler.handle_body_type(bot, callback)

        elif callback.data in [CALLBACK_DATA_GEARBOX_TYPE_AUTOMATIC, CALLBACK_DATA_GEARBOX_TYPE_MECHANICAL,
                               CALLBACK_DATA_GEARBOX_TYPE_OTHER]:
            addvertisement_handler.handle_gearbox_type(bot, callback)

        elif callback.data in [CALLBACK_DATA_COLOR_BLACK, CALLBACK_DATA_COLOR_WHITE, CALLBACK_DATA_COLOR_GREY,
                               CALLBACK_DATA_COLOR_CYAN, CALLBACK_DATA_COLOR_RED, CALLBACK_DATA_COLOR_BLUE,
                               CALLBACK_DATA_COLOR_BEIGE, CALLBACK_DATA_COLOR_SILVER, CALLBACK_DATA_COLOR_GREEN,
                               CALLBACK_DATA_COLOR_BROWN, CALLBACK_DATA_COLOR_OTHER]:
            addvertisement_handler.handle_color(bot, callback)

        elif callback.data in [CALLBACK_DATA_FUEL_TYPE_PETROL, CALLBACK_DATA_FUEL_TYPE_GAS,
                               CALLBACK_DATA_FUEL_TYPE_ELECTRO, CALLBACK_DATA_FUEL_TYPE_HYBRID,
                               CALLBACK_DATA_FUEL_TYPE_PETROL_GAS]:
            addvertisement_handler.handle_fuel_type(bot, callback)

        elif callback.data in [CALLBACK_DATA_MACHINE_CONDITION_EXCELLENT, CALLBACK_DATA_MACHINE_CONDITION_GOOD,
                               CALLBACK_DATA_MACHINE_CONDITION_AVERAGE, CALLBACK_DATA_MACHINE_CONDITION_NEEDS_REPAIR]:
            addvertisement_handler.handle_machine_condition(bot, callback)

        elif callback.data in [CALLBACK_DATA_NUMBER_OF_OWNERS_1, CALLBACK_DATA_NUMBER_OF_OWNERS_2,
                               CALLBACK_DATA_NUMBER_OF_OWNERS_3, CALLBACK_DATA_NUMBER_OF_OWNERS_OTHER]:
            addvertisement_handler.handle_number_of_owners(bot, callback)

        elif callback.data in [CALLBACK_DATA_CITY_TASHKENT, CALLBACK_DATA_CITY_SAMARKAND, CALLBACK_DATA_CITY_ANDIJAN,
                               CALLBACK_DATA_CITY_FERGANA, CALLBACK_DATA_CITY_BUKHARA, CALLBACK_DATA_CITY_OTHER]:
            addvertisement_handler.handle_city(bot, callback)

        elif callback.data in [CALLBACK_DATA_PAYMENT_TYPE_CASH, CALLBACK_DATA_PAYMENT_TYPE_LEASING,
                               CALLBACK_DATA_PAYMENT_TYPE_TRANSFER, CALLBACK_DATA_PAYMENT_TYPE_CREDIT,
                               CALLBACK_DATA_PAYMENT_TYPE_INSTALLMENT]:
            addvertisement_handler.handle_payment_type(bot, callback)

        bot.answer_callback_query(callback.id)
