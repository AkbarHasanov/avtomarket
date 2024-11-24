from telebot import types
from const import CALLBACK_DATA_CLICK, CALLBACK_DATA_PAYME
from bot.repository.tariff import get_by_callback_data

from bot.repository.user import *
from bot.repository.car import *
from config import *


def choose_payment_system(bot, callback):
    user = get_user_by_chat_id(callback.message.chat.id)
    car = get_last_car_by_user_id(user.id)
    tariff = get_by_callback_data(callback.data)
    update_tariff(car, tariff.id)

    markup = types.InlineKeyboardMarkup()

    markup.add(types.InlineKeyboardButton("CLICK Uzbekistan", callback_data=CALLBACK_DATA_CLICK))
    markup.add(types.InlineKeyboardButton("PayMe", callback_data=CALLBACK_DATA_PAYME))

    text = {
        UZBEK_LANGUAGE: "Toʻlov usulini tanlang.",
        RUSSIAN_LANGUAGE: "Выберете способ оплаты."
    }

    bot.send_message(callback.message.chat.id, text=text[user.language], reply_markup=markup)
