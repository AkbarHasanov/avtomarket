from functools import partial

from bot.models.car import Car
from telebot import TeleBot, types
from bot.const import CALLBACK_DATA_ADD_PHOTOS, CALLBACK_DATA_ADD_ADVERTISEMENT

from bot.repository.user import *
from bot.repository.car import *
from config import UZBEK_LANGUAGE, RUSSIAN_LANGUAGE


def add_advertisement(bot, callback):
    user = get_user_by_chat_id(callback.message.chat.id)

    car = Car(user_id=user.id)

    text = {
        UZBEK_LANGUAGE: "Sotish haqida e'lon qilish uchun mashina haqida bosqichma-bosqich anketani to'ldiring 🚘.",
        RUSSIAN_LANGUAGE: "Пожалуйста, заполните пошагово анкету об автомобиле для рекламы о продаже 🚘."
    }

    bot.send_message(callback.message.chat.id, text=text[user.language])

    text = {
        UZBEK_LANGUAGE: "Avtomobil modeli va markasi:",
        RUSSIAN_LANGUAGE: "Модель и марка машины:"
    }

    msg = bot.send_message(callback.message.chat.id, text=text[user.language])
    bot.register_next_step_handler(msg, partial(get_model, bot=bot, language=user.language, car=car))


def get_model(message, bot: TeleBot, car: Car, language: str):
    car.model = message.text

    text = {
        UZBEK_LANGUAGE: "Narxi:",
        RUSSIAN_LANGUAGE: "Цена:"
    }
    msg = bot.send_message(message.chat.id, text=text[language])
    bot.register_next_step_handler(msg, partial(get_price, bot=bot, language=language, car=car))


def get_price(message, bot: TeleBot, car: Car, language: str):
    car.price = int(message.text)
    text = {
        UZBEK_LANGUAGE: "Tana turi:",
        RUSSIAN_LANGUAGE: "Тип кузова:"
    }

    msg = bot.send_message(message.chat.id, text=text[language])
    bot.register_next_step_handler(msg, partial(get_body_type, bot=bot, language=language, car=car))


def get_body_type(message, bot: TeleBot, car: Car, language: str):
    car.body_type = message.text
    text = {
        UZBEK_LANGUAGE: 'Ishlab chiqarilgan yili:',
        RUSSIAN_LANGUAGE: "Пробег:"
    }

    msg = bot.send_message(message.chat.id, text=text[language])
    bot.register_next_step_handler(msg, partial(get_mileage, bot=bot, language=language, car=car))


def get_mileage(message, bot: TeleBot, car: Car, language: str):
    car.mileage = message.text
    text = {
        UZBEK_LANGUAGE: 'Vites qutisi turi:',
        RUSSIAN_LANGUAGE: "Тип коробки передач:"
    }

    msg = bot.send_message(message.chat.id, text=text[language])
    bot.register_next_step_handler(msg, partial(get_gearbox_type, bot=bot, language=language, car=car))


def get_gearbox_type(message, bot: TeleBot, car: Car, language: str):
    car.gearbox_type = message.text
    text = {
        UZBEK_LANGUAGE: 'Chiqarilgan yili:',
        RUSSIAN_LANGUAGE: "Год выпуска:"
    }

    msg = bot.send_message(message.chat.id, text=text[language])
    bot.register_next_step_handler(msg, partial(get_issue_year, bot=bot, language=language, car=car))


def get_issue_year(message, bot: TeleBot, car: Car, language: str):
    car.issue_year = message.text
    text = {
        UZBEK_LANGUAGE: 'Rang:',
        RUSSIAN_LANGUAGE: "Цвет:"
    }

    msg = bot.send_message(message.chat.id, text=text[language])
    bot.register_next_step_handler(msg, partial(get_color, bot=bot, language=language, car=car))


def get_color(message, bot: TeleBot, car: Car, language: str):
    car.color = message.text
    text = {
        UZBEK_LANGUAGE: 'Dvigatel hajmi:',
        RUSSIAN_LANGUAGE: "Объем двигателя:"
    }

    msg = bot.send_message(message.chat.id, text=text[language])
    bot.register_next_step_handler(msg, partial(get_engine_capacity, bot=bot, language=language, car=car))


def get_engine_capacity(message, bot: TeleBot, car: Car, language: str):
    car.engine_capacity = message.text
    text = {
        UZBEK_LANGUAGE: "Yoqilg'i turi:",
        RUSSIAN_LANGUAGE: "Вид топлива:"
    }

    msg = bot.send_message(message.chat.id, text=text[language])
    bot.register_next_step_handler(msg, partial(get_fuel_type, bot=bot, language=language, car=car))


def get_fuel_type(message, bot: TeleBot, car: Car, language: str):
    car.fuel_type = message.text
    text = {
        UZBEK_LANGUAGE: 'Avtomobil holati:',
        RUSSIAN_LANGUAGE: "Состояние машины:"
    }

    msg = bot.send_message(message.chat.id, text=text[language])
    bot.register_next_step_handler(msg, partial(get_machine_condition, bot=bot, language=language, car=car))


def get_machine_condition(message, bot: TeleBot, car: Car, language: str):
    car.machine_condition = message.text
    text = {
        UZBEK_LANGUAGE: 'Egalari soni:',
        RUSSIAN_LANGUAGE: "Количество владельцев:"
    }

    msg = bot.send_message(message.chat.id, text=text[language])
    bot.register_next_step_handler(msg, partial(get_number_of_owners, bot=bot, language=language, car=car))


def get_number_of_owners(message, bot: TeleBot, car: Car, language: str):
    car.number_of_owners = message.text
    text = {
        UZBEK_LANGUAGE: 'Aloqa telefon raqami:',
        RUSSIAN_LANGUAGE: "Qo'shimcha variantlar:"
    }

    msg = bot.send_message(message.chat.id, text=text[language])
    bot.register_next_step_handler(msg, partial(get_phone_number, bot=bot, language=language, car=car))


def get_phone_number(message, bot: TeleBot, car: Car, language: str):
    car.phone_number = message.text
    text = {
        UZBEK_LANGUAGE: 'Shahar:',
        RUSSIAN_LANGUAGE: "Город:"
    }

    msg = bot.send_message(message.chat.id, text=text[language])
    bot.register_next_step_handler(msg, partial(get_city, bot=bot, language=language, car=car))


def get_city(message, bot: TeleBot, car: Car, language: str):
    car.city = message.text
    text = {
        UZBEK_LANGUAGE: "To'lov turi:",
        RUSSIAN_LANGUAGE: "Выберете вид оплаты, доступны такие виды как (Наличка/Кредит/Лизинг/Рассрочка):"
    }

    msg = bot.send_message(message.chat.id, text=text[language])
    bot.register_next_step_handler(msg, partial(get_payment_type, bot=bot, language=language, car=car))


def get_payment_type(message, bot: TeleBot, car: Car, language: str):
    car.payment_type = message.text
    text = {
        UZBEK_LANGUAGE: "Qo'shimcha variantlar:",
        RUSSIAN_LANGUAGE: "Доп. Опции:"
    }

    msg = bot.send_message(message.chat.id, text=text[language])
    bot.register_next_step_handler(msg, partial(get_additional_options, bot=bot, language=language, car=car))


def get_additional_options(message, bot: TeleBot, car: Car, language: str):
    car.additional_options = message.text
    create_car(car)

    text = {
        UZBEK_LANGUAGE: f"""🔥{car.model}-{car.price}🔥
        
        ▪️Avtomobil modeli va markasi: {car.model}
        ▪️Narxi: {car.price}
        ▪️Tana turi: {car.body_type}
        ▪️Ishlab chiqarilgan yili: {car.issue_year}
        ▪️️Yurgan masofasi: {car.mileage}
        ▪️Vites qutisi turi: {car.gearbox_type}
        ▪️Rang: {car.color}
        ▪️Dvigatel hajmi: {car.engine_capacity}
        ▪️Yoqilg'i turi: {car.fuel_type}
        ▪️Avtomobil holati: {car.machine_condition}
        ▪️Egalari soni: {car.number_of_owners}
        ▪️Shahar: {car.city}
        ▪️To'lov turi: {car.payment_type}
        ▪️Aloqa telefon raqami: {car.phone_number}
        
        
        ▪️Qo'shimcha variantlar: {car.additional_options}""",
        RUSSIAN_LANGUAGE: f"""🔥{car.model}-{car.price}🔥
        
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
        ▪️Город: {car.city}
        ▪️Вид оплаты: {car.payment_type}
        ▪️Телефон для связи: {car.phone_number}
        
        
        ▪️Доп. Опции: {car.additional_options}"""
    }

    bot.send_message(message.chat.id, text=text[language])

    markup = types.InlineKeyboardMarkup()
    text = {
        UZBEK_LANGUAGE: "Hammasi to'g'ri✅",
        RUSSIAN_LANGUAGE: "Все верно✅"
    }
    err = {
        UZBEK_LANGUAGE: "Xato❌",
        RUSSIAN_LANGUAGE: "Ошибка❌"
    }
    markup.add(types.InlineKeyboardButton(text[language], callback_data=CALLBACK_DATA_ADD_PHOTOS))
    markup.add(types.InlineKeyboardButton(err[language], callback_data=CALLBACK_DATA_ADD_ADVERTISEMENT))

    text = {
        UZBEK_LANGUAGE: "Iltimos, mashinangiz tafsilotlarini tekshiring.",
        RUSSIAN_LANGUAGE: "Пожалуйста проверьте данные о машине."
    }
    bot.send_message(message.chat.id, text=text[language], reply_markup=markup)


def add_photo(bot, callback):
    user = get_user_by_chat_id(callback.message.chat.id)

    text = {
        UZBEK_LANGUAGE: "Davom etish uchun mashinaning 6 ta fotosuratini yuboring.",
        RUSSIAN_LANGUAGE: "Для того чтобы продолжить отправьте 6 фотографий автомобиля."
    }

    bot.send_message(callback.message.chat.id, text=text[user.language])
