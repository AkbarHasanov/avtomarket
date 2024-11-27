import base64

from telebot import types

from bot.repository.tariff import get_translation

from bot.repository.user import *
from bot.repository.car import *
from config import *


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


def send_payment_success_message(bot, car: Car):
    user = get(car.user_id)

    tariff_detail = get_translation(car.tariff_id, user.language)
    bot.send_message(ADMIN_CHAT_ID,
                     f"""Клиет купил тариф: {tariff_detail.name}\nИмя пользователя @{user.username}""")

    photos = []
    for i, photo in enumerate(car.photos):
        caption = None
        if i == len(car.photos) - 1:
            caption = f"""🔥{car.model}-{car.price}🔥
            
            ▪️Модель и марка машины: {car.model}
            ▪️Цена: {car.price}
            ▪️Тип кузова: {car.body_type}
            ▪️Год выпуска: {car.issue_year}
            ▪️Пробег: {car.mileage}
            ▪️Тип коробки передач: {car.gearbox_type}
            ▪️Цвет: {car.color}
            ▪️Объем двигателя: {car.engine_capacity}
            ▪️Вид топлива: {car.fuel_type}
            ▪️Состояние машины: {car.machine_condition}
            ▪️Количество владельцев: {car.number_of_owners}
            ▪️Телефон для связи: {car.phone_number}
            ▪️Город: {car.city}
            ▪️Вид оплаты: {car.payment_type}"""

        photos.append(types.InputMediaPhoto(photo.path, caption=caption))

    bot.send_media_group(ADMIN_CHAT_ID, media=photos)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton("Сообщить о продаже машины 🚘")
    btn2 = types.KeyboardButton("Дать рекламное обьявление 🛍")
    btn3 = types.KeyboardButton("Нужна помощь с другим вопросом ❓")
    markup.add(btn1, btn2, btn3)
    bot.send_message(user.chat_id,
                     """Спасибо за доверие! Ваше объявление о продаже автомобиля будет опубликовано в кратчайшие сроки.
                     
                     Пожалуйста, сообщите нам после продажи автомобиля 🙏🏻
                     
                     Если ваш пост не будет опубликован в течении 24 часов, прошу связаться с Админом.""",
                     reply_markup=markup)