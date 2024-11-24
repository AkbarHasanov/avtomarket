import base64

from telebot import types
from const import CALLBACK_DATA_CLICK, CALLBACK_DATA_PAYME
from bot.repository.tariff import get_translation, get_by_callback_data

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


def click_payment(bot, callback):
    user = get_user_by_chat_id(callback.message.chat.id)
    car = get_last_car_by_user_id(user.id)
    tariff_detail = get_translation(car.tariff_id, user.language)

    url = f"""https://my.click.uz/services/pay?service_id={CLICK_SERVICE_ID}&merchant_id={CLICK_MERCHANT_ID}&amount={car.tariff.amount * 100}&transaction_param={car.id}&return_url={RETURN_URL}"""

    markup = types.InlineKeyboardMarkup()
    payment_button = types.InlineKeyboardButton(
        text=tariff_detail.title,
        url=url
    )
    markup.add(payment_button)

    bot.send_message(
        callback.message.chat.id,
        tariff_detail.description,
        reply_markup=markup
    )


def payme_payment(bot, callback):
    user = get_user_by_chat_id(callback.message.chat.id)
    car = get_last_car_by_user_id(user.id)
    tariff_detail = get_translation(car.tariff_id, user.language)

    request_data = f"m={PAYME_MERCHANT_ID};ac.order_id={car.id};a={car.tariff.amount * 100};l=uz;c={RETURN_URL};ct=1000;cr=UZS"
    data_bytes = request_data.encode('utf-8')
    base64_encoded = base64.b64encode(data_bytes).decode('utf-8')
    url = f"""{PAYME_URI}/{base64_encoded}"""

    markup = types.InlineKeyboardMarkup()
    payment_button = types.InlineKeyboardButton(
        text=tariff_detail.title,
        url=url
    )
    markup.add(payment_button)

    bot.send_message(
        callback.message.chat.id,
        tariff_detail.description,
        reply_markup=markup
    )
