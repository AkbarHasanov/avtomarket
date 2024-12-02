from functools import partial

from telebot import TeleBot, types
from const import *

from bot.repository.user import *
from bot.repository.car import *
from config import UZBEK_LANGUAGE, RUSSIAN_LANGUAGE

body_type = {
    CALLBACK_DATA_BODY_TYPE_SEDAN: {
        UZBEK_LANGUAGE: "Sedan",
        RUSSIAN_LANGUAGE: "Седан"
    },
    CALLBACK_DATA_BODY_TYPE_COUPE: {
        UZBEK_LANGUAGE: "Kupe",
        RUSSIAN_LANGUAGE: "Купе"
    },
    CALLBACK_DATA_BODY_TYPE_HATCHBACK: {
        UZBEK_LANGUAGE: "Xetchbek",
        RUSSIAN_LANGUAGE: "Хэтчбек"
    },
    CALLBACK_DATA_BODY_TYPE_UNIVERSAL: {
        UZBEK_LANGUAGE: "Krossover",
        RUSSIAN_LANGUAGE: "Кроссовер"
    },
    CALLBACK_DATA_BODY_TYPE_CROSSOVER: {
        UZBEK_LANGUAGE: "SUV",
        RUSSIAN_LANGUAGE: "Внедорожник"
    },
    CALLBACK_DATA_BODY_TYPE_SUV: {
        UZBEK_LANGUAGE: "Stansiya vagoni",
        RUSSIAN_LANGUAGE: "Универсал"
    },
    CALLBACK_DATA_BODY_TYPE_OTHER: {
        UZBEK_LANGUAGE: "Boshqa",
        RUSSIAN_LANGUAGE: "Другое"
    }
}

gearbox_type = {
    CALLBACK_DATA_GEARBOX_TYPE_AUTOMATIC: {
        UZBEK_LANGUAGE: "Avtomatik",
        RUSSIAN_LANGUAGE: "Автоматическая"
    },
    CALLBACK_DATA_GEARBOX_TYPE_MECHANICAL: {
        UZBEK_LANGUAGE: "Mexanik",
        RUSSIAN_LANGUAGE: "Механическая"
    },
    CALLBACK_DATA_GEARBOX_TYPE_OTHER: {
        UZBEK_LANGUAGE: "Boshqa",
        RUSSIAN_LANGUAGE: "Другое"
    }
}

color = {
    CALLBACK_DATA_COLOR_BLACK: {
        UZBEK_LANGUAGE: "Qora",
        RUSSIAN_LANGUAGE: "Черный"
    },
    CALLBACK_DATA_COLOR_WHITE: {
        UZBEK_LANGUAGE: "Oq",
        RUSSIAN_LANGUAGE: "Белый"
    },
    CALLBACK_DATA_COLOR_GREY: {
        UZBEK_LANGUAGE: "Kulrang",
        RUSSIAN_LANGUAGE: "Серый"
    },
    CALLBACK_DATA_COLOR_CYAN: {
        UZBEK_LANGUAGE: "Moviy",
        RUSSIAN_LANGUAGE: "Голубой"
    },
    CALLBACK_DATA_COLOR_RED: {
        UZBEK_LANGUAGE: "Qizil",
        RUSSIAN_LANGUAGE: "Красный"
    },
    CALLBACK_DATA_COLOR_BLUE: {
        UZBEK_LANGUAGE: "Ko’k",
        RUSSIAN_LANGUAGE: "Синий"
    },
    CALLBACK_DATA_COLOR_BEIGE: {
        UZBEK_LANGUAGE: "Bej",
        RUSSIAN_LANGUAGE: "Бежевый"
    },
    CALLBACK_DATA_COLOR_SILVER: {
        UZBEK_LANGUAGE: "Kumush",
        RUSSIAN_LANGUAGE: "Серебристый"
    },
    CALLBACK_DATA_COLOR_GREEN: {
        UZBEK_LANGUAGE: "Yashil",
        RUSSIAN_LANGUAGE: "Зеленый"
    },
    CALLBACK_DATA_COLOR_BROWN: {
        UZBEK_LANGUAGE: "Jigarrang",
        RUSSIAN_LANGUAGE: "Коричневый"
    },
    CALLBACK_DATA_COLOR_OTHER: {
        UZBEK_LANGUAGE: "Boshqa",
        RUSSIAN_LANGUAGE: "Другой"
    },
}

fuel_type = {
    CALLBACK_DATA_FUEL_TYPE_PETROL: {
        UZBEK_LANGUAGE: "Benzin",
        RUSSIAN_LANGUAGE: "Бензин"
    },
    CALLBACK_DATA_FUEL_TYPE_GAS: {
        UZBEK_LANGUAGE: "Gaz",
        RUSSIAN_LANGUAGE: "Газ"
    },
    CALLBACK_DATA_FUEL_TYPE_ELECTRO: {
        UZBEK_LANGUAGE: "Elektro",
        RUSSIAN_LANGUAGE: "Электро"
    },
    CALLBACK_DATA_FUEL_TYPE_HYBRID: {
        UZBEK_LANGUAGE: "Gibrid",
        RUSSIAN_LANGUAGE: "Гибрид"
    },
    CALLBACK_DATA_FUEL_TYPE_PETROL_GAS: {
        UZBEK_LANGUAGE: "Gaz/benzin",
        RUSSIAN_LANGUAGE: "Газ/Бензин"
    },
}

machine_condition = {
    CALLBACK_DATA_MACHINE_CONDITION_EXCELLENT: {
        UZBEK_LANGUAGE: "A’lo",
        RUSSIAN_LANGUAGE: "Отличное"
    },
    CALLBACK_DATA_MACHINE_CONDITION_GOOD: {
        UZBEK_LANGUAGE: "Yaxshi",
        RUSSIAN_LANGUAGE: "Хорошее"
    },
    CALLBACK_DATA_MACHINE_CONDITION_AVERAGE: {
        UZBEK_LANGUAGE: "O'rtacha",
        RUSSIAN_LANGUAGE: "Среднее"
    },
    CALLBACK_DATA_MACHINE_CONDITION_NEEDS_REPAIR: {
        UZBEK_LANGUAGE: "Ta'mirlash kerak",
        RUSSIAN_LANGUAGE: "Требует ремонта"
    },
}

number_of_owners = {
    CALLBACK_DATA_NUMBER_OF_OWNERS_1: {
        UZBEK_LANGUAGE: "1",
        RUSSIAN_LANGUAGE: "1"
    },
    CALLBACK_DATA_NUMBER_OF_OWNERS_2: {
        UZBEK_LANGUAGE: "2",
        RUSSIAN_LANGUAGE: "2"
    },
    CALLBACK_DATA_NUMBER_OF_OWNERS_3: {
        UZBEK_LANGUAGE: "3",
        RUSSIAN_LANGUAGE: "3"
    },
    CALLBACK_DATA_NUMBER_OF_OWNERS_OTHER: {
        UZBEK_LANGUAGE: "Boshqa",
        RUSSIAN_LANGUAGE: "Другой"
    },
}

city = {
    CALLBACK_DATA_CITY_TASHKENT: {
        UZBEK_LANGUAGE: "Toshkent",
        RUSSIAN_LANGUAGE: "Ташкент"
    },
    CALLBACK_DATA_CITY_SAMARKAND: {
        UZBEK_LANGUAGE: "Samarqand",
        RUSSIAN_LANGUAGE: "Самарканд"
    },
    CALLBACK_DATA_CITY_ANDIJAN: {
        UZBEK_LANGUAGE: "Andijon",
        RUSSIAN_LANGUAGE: "Андижан"
    },
    CALLBACK_DATA_CITY_FERGANA: {
        UZBEK_LANGUAGE: "Farg'ona",
        RUSSIAN_LANGUAGE: "Фергана"
    },
    CALLBACK_DATA_CITY_BUKHARA: {
        UZBEK_LANGUAGE: "Buxoro",
        RUSSIAN_LANGUAGE: "Бухара"
    },
    CALLBACK_DATA_CITY_OTHER: {
        UZBEK_LANGUAGE: "Boshqa",
        RUSSIAN_LANGUAGE: "Другой"
    },
}

payment_types = {
    CALLBACK_DATA_PAYMENT_TYPE_CASH: {
        UZBEK_LANGUAGE: "Naqd pul",
        RUSSIAN_LANGUAGE: "Наличными"
    },
    CALLBACK_DATA_PAYMENT_TYPE_LEASING: {
        UZBEK_LANGUAGE: "Lizing",
        RUSSIAN_LANGUAGE: "Лизинг"
    },
    CALLBACK_DATA_PAYMENT_TYPE_TRANSFER: {
        UZBEK_LANGUAGE: "Perechisleniye",
        RUSSIAN_LANGUAGE: "Перечисление"
    },
    CALLBACK_DATA_PAYMENT_TYPE_CREDIT: {
        UZBEK_LANGUAGE: "Kredit",
        RUSSIAN_LANGUAGE: "Кредит"
    },
    CALLBACK_DATA_PAYMENT_TYPE_INSTALLMENT: {
        UZBEK_LANGUAGE: "Rassrochka (variant)",
        RUSSIAN_LANGUAGE: "Рассрочка (Вариант)"
    },
}


def add_advertisement(bot, callback: types.CallbackQuery):
    user = get_user_by_chat_id(callback.message.chat.id)

    car = Car(user_id=user.id)
    create_car(car)

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
    set_model(car.id, message.text)

    text = {
        UZBEK_LANGUAGE: "Narxi:",
        RUSSIAN_LANGUAGE: "Цена:"
    }
    msg = bot.send_message(message.chat.id, text=text[language])
    bot.register_next_step_handler(msg, partial(get_price, bot=bot, language=language, car=car))


def get_price(message: types.Message, bot: TeleBot, car: Car, language: str):
    car.price = message.text
    set_price(car.id, message.text)

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(body_type[CALLBACK_DATA_BODY_TYPE_SEDAN][language],
                                          callback_data=CALLBACK_DATA_BODY_TYPE_SEDAN))
    markup.add(types.InlineKeyboardButton(body_type[CALLBACK_DATA_BODY_TYPE_COUPE][language],
                                          callback_data=CALLBACK_DATA_BODY_TYPE_COUPE))
    markup.add(types.InlineKeyboardButton(body_type[CALLBACK_DATA_BODY_TYPE_HATCHBACK][language],
                                          callback_data=CALLBACK_DATA_BODY_TYPE_HATCHBACK))
    markup.add(types.InlineKeyboardButton(body_type[CALLBACK_DATA_BODY_TYPE_UNIVERSAL][language],
                                          callback_data=CALLBACK_DATA_BODY_TYPE_UNIVERSAL))
    markup.add(types.InlineKeyboardButton(body_type[CALLBACK_DATA_BODY_TYPE_CROSSOVER][language],
                                          callback_data=CALLBACK_DATA_BODY_TYPE_CROSSOVER))
    markup.add(types.InlineKeyboardButton(body_type[CALLBACK_DATA_BODY_TYPE_SUV][language],
                                          callback_data=CALLBACK_DATA_BODY_TYPE_SUV))
    markup.add(types.InlineKeyboardButton(body_type[CALLBACK_DATA_BODY_TYPE_OTHER][UZBEK_LANGUAGE],
                                          callback_data=CALLBACK_DATA_BODY_TYPE_OTHER))
    text = {
        UZBEK_LANGUAGE: "Kuzov turi:",
        RUSSIAN_LANGUAGE: "Тип кузова:"
    }

    bot.send_message(message.chat.id, text=text[language], reply_markup=markup)


def get_body_type(message, bot: TeleBot, car: Car, language: str):
    car.body_type = message.text
    set_body_type(car.id, message.text)

    text = {
        UZBEK_LANGUAGE: 'Kilometr:',
        RUSSIAN_LANGUAGE: "Пробег:"
    }

    msg = bot.send_message(message.chat.id, text=text[language])
    bot.register_next_step_handler(msg, partial(get_mileage, bot=bot, language=language, car=car))


def get_mileage(message, bot: TeleBot, car: Car, language: str):
    car.mileage = message.text
    set_mileage(car.id, message.text)

    markup = types.InlineKeyboardMarkup()
    automatic = types.InlineKeyboardButton(gearbox_type[CALLBACK_DATA_GEARBOX_TYPE_AUTOMATIC][language],
                                           callback_data=CALLBACK_DATA_GEARBOX_TYPE_AUTOMATIC)
    mechanical = types.InlineKeyboardButton(gearbox_type[CALLBACK_DATA_GEARBOX_TYPE_MECHANICAL][language],
                                            callback_data=CALLBACK_DATA_GEARBOX_TYPE_MECHANICAL)
    other = types.InlineKeyboardButton(gearbox_type[CALLBACK_DATA_GEARBOX_TYPE_OTHER][language],
                                       callback_data=CALLBACK_DATA_GEARBOX_TYPE_OTHER)
    markup.add(automatic, mechanical, other)

    text = {
        UZBEK_LANGUAGE: 'Uzatmalar qutisi:',
        RUSSIAN_LANGUAGE: "Тип коробки передач:"
    }

    bot.send_message(message.chat.id, text=text[language], reply_markup=markup)


def get_gearbox_type(message, bot: TeleBot, car: Car, language: str):
    car.gearbox_type = message.text
    set_gearbox_type(car.id, message.text)

    text = {
        UZBEK_LANGUAGE: 'Chiqarilgan yili:',
        RUSSIAN_LANGUAGE: "Год выпуска:"
    }

    msg = bot.send_message(message.chat.id, text=text[language])
    bot.register_next_step_handler(msg, partial(get_issue_year, bot=bot, language=language, car=car))


def get_issue_year(message, bot: TeleBot, car: Car, language: str):
    car.issue_year = message.text
    set_issue_year(car.id, message.text)

    markup = types.InlineKeyboardMarkup()
    black = types.InlineKeyboardButton(color[CALLBACK_DATA_COLOR_BLACK][language],
                                       callback_data=CALLBACK_DATA_COLOR_BLACK)
    white = types.InlineKeyboardButton(color[CALLBACK_DATA_COLOR_WHITE][language],
                                       callback_data=CALLBACK_DATA_COLOR_WHITE)
    grey = types.InlineKeyboardButton(color[CALLBACK_DATA_COLOR_GREY][language],
                                      callback_data=CALLBACK_DATA_COLOR_GREY)
    cyan = types.InlineKeyboardButton(color[CALLBACK_DATA_COLOR_CYAN][language],
                                      callback_data=CALLBACK_DATA_COLOR_CYAN)
    red = types.InlineKeyboardButton(color[CALLBACK_DATA_COLOR_RED][language],
                                     callback_data=CALLBACK_DATA_COLOR_RED)
    blue = types.InlineKeyboardButton(color[CALLBACK_DATA_COLOR_BLUE][language],
                                      callback_data=CALLBACK_DATA_COLOR_BLUE)
    beige = types.InlineKeyboardButton(color[CALLBACK_DATA_COLOR_BEIGE][language],
                                       callback_data=CALLBACK_DATA_COLOR_BEIGE)
    silver = types.InlineKeyboardButton(color[CALLBACK_DATA_COLOR_SILVER][language],
                                        callback_data=CALLBACK_DATA_COLOR_SILVER)
    green = types.InlineKeyboardButton(color[CALLBACK_DATA_COLOR_GREEN][language],
                                       callback_data=CALLBACK_DATA_COLOR_GREEN)
    brown = types.InlineKeyboardButton(color[CALLBACK_DATA_COLOR_BROWN][language],
                                       callback_data=CALLBACK_DATA_COLOR_BROWN)
    other = types.InlineKeyboardButton(color[CALLBACK_DATA_COLOR_OTHER][language],
                                       callback_data=CALLBACK_DATA_COLOR_OTHER)

    markup.add(black, white, grey, cyan, red, blue, beige, silver, green, brown, other)

    text = {
        UZBEK_LANGUAGE: 'Rang:',
        RUSSIAN_LANGUAGE: "Цвет:"
    }

    bot.send_message(message.chat.id, text=text[language], reply_markup=markup)


def get_color(message, bot: TeleBot, car: Car, language: str):
    car.color = message.text
    set_color(car.id, message.text)

    text = {
        UZBEK_LANGUAGE: 'Dvigatel hajmi:',
        RUSSIAN_LANGUAGE: "Объем двигателя:"
    }

    msg = bot.send_message(message.chat.id, text=text[language])
    bot.register_next_step_handler(msg, partial(get_engine_capacity, bot=bot, language=language, car=car))


def get_engine_capacity(message, bot: TeleBot, car: Car, language: str):
    car.engine_capacity = message.text
    set_engine_capacity(car.id, message.text)

    markup = types.InlineKeyboardMarkup()
    petrol = types.InlineKeyboardButton(fuel_type[CALLBACK_DATA_FUEL_TYPE_PETROL][language],
                                        callback_data=CALLBACK_DATA_FUEL_TYPE_PETROL)
    gas = types.InlineKeyboardButton(fuel_type[CALLBACK_DATA_FUEL_TYPE_GAS][language],
                                     callback_data=CALLBACK_DATA_FUEL_TYPE_GAS)
    electro = types.InlineKeyboardButton(fuel_type[CALLBACK_DATA_FUEL_TYPE_ELECTRO][language],
                                         callback_data=CALLBACK_DATA_FUEL_TYPE_ELECTRO)
    hybrid = types.InlineKeyboardButton(fuel_type[CALLBACK_DATA_FUEL_TYPE_HYBRID][language],
                                        callback_data=CALLBACK_DATA_FUEL_TYPE_HYBRID)
    petrol_gas = types.InlineKeyboardButton(fuel_type[CALLBACK_DATA_FUEL_TYPE_PETROL_GAS][language],
                                            callback_data=CALLBACK_DATA_FUEL_TYPE_PETROL_GAS)

    markup.add(petrol, gas, electro, hybrid, petrol_gas)

    text = {
        UZBEK_LANGUAGE: "Yoqilg'i turi:",
        RUSSIAN_LANGUAGE: "Вид топлива:"
    }

    bot.send_message(message.chat.id, text=text[language], reply_markup=markup)


def get_number_of_owners(message, bot: TeleBot, car: Car, language: str):
    car.number_of_owners = message.text
    set_number_of_owners(car.id, message.text)

    text = {
        UZBEK_LANGUAGE: 'Aloqa telefon raqami:',
        RUSSIAN_LANGUAGE: "Телефон для связи:"
    }

    msg = bot.send_message(message.chat.id, text=text[language])
    bot.register_next_step_handler(msg, partial(get_phone_number, bot=bot, language=language, car=car))


def get_phone_number(message, bot: TeleBot, car: Car, language: str):
    car.phone_number = message.text
    set_phone_number(car.id, message.text)

    markup = types.InlineKeyboardMarkup()
    tashkent = types.InlineKeyboardButton(city[CALLBACK_DATA_CITY_TASHKENT][language],
                                          callback_data=CALLBACK_DATA_CITY_TASHKENT)
    samarkand = types.InlineKeyboardButton(city[CALLBACK_DATA_CITY_SAMARKAND][language],
                                           callback_data=CALLBACK_DATA_CITY_SAMARKAND)
    andijan = types.InlineKeyboardButton(city[CALLBACK_DATA_CITY_ANDIJAN][language],
                                         callback_data=CALLBACK_DATA_CITY_ANDIJAN)
    fergana = types.InlineKeyboardButton(city[CALLBACK_DATA_CITY_FERGANA][language],
                                         callback_data=CALLBACK_DATA_CITY_FERGANA)
    bukhara = types.InlineKeyboardButton(city[CALLBACK_DATA_CITY_BUKHARA][language],
                                         callback_data=CALLBACK_DATA_CITY_BUKHARA)
    other = types.InlineKeyboardButton(city[CALLBACK_DATA_CITY_OTHER][language], callback_data=CALLBACK_DATA_CITY_OTHER)
    markup.add(tashkent, samarkand, andijan, fergana, bukhara, other)

    text = {
        UZBEK_LANGUAGE: 'Shahar:',
        RUSSIAN_LANGUAGE: "Город:"
    }

    bot.send_message(message.chat.id, text=text[language], reply_markup=markup)


def get_city(message, bot: TeleBot, car: Car, language: str):
    car.city = message.text
    set_city(car.id, message.text)

    markup = types.InlineKeyboardMarkup()
    cash = types.InlineKeyboardButton(payment_types[CALLBACK_DATA_PAYMENT_TYPE_CASH][language],
                                      callback_data=CALLBACK_DATA_PAYMENT_TYPE_CASH)
    leasing = types.InlineKeyboardButton(payment_types[CALLBACK_DATA_PAYMENT_TYPE_LEASING][language],
                                         callback_data=CALLBACK_DATA_PAYMENT_TYPE_LEASING)
    transfer = types.InlineKeyboardButton(payment_types[CALLBACK_DATA_PAYMENT_TYPE_TRANSFER][language],
                                          callback_data=CALLBACK_DATA_PAYMENT_TYPE_TRANSFER)
    credit = types.InlineKeyboardButton(payment_types[CALLBACK_DATA_PAYMENT_TYPE_CREDIT][language],
                                        callback_data=CALLBACK_DATA_PAYMENT_TYPE_CREDIT)
    installment = types.InlineKeyboardButton(payment_types[CALLBACK_DATA_PAYMENT_TYPE_INSTALLMENT][language],
                                             callback_data=CALLBACK_DATA_PAYMENT_TYPE_INSTALLMENT)
    markup.add(cash, leasing, transfer, credit, installment)

    text = {
        UZBEK_LANGUAGE: "To'lov turi:",
        RUSSIAN_LANGUAGE: "Выберете вид оплаты, доступны такие виды как (Наличка/Кредит/Лизинг/Рассрочка):"
    }

    bot.send_message(message.chat.id, text=text[language], reply_markup=markup)


def get_payment_type(message, bot: TeleBot, car: Car, language: str):
    car.payment_type = message.text
    set_payment_type(car.id, message.text)

    text = {
        UZBEK_LANGUAGE: "Qo'shimcha variantlar:",
        RUSSIAN_LANGUAGE: "Доп. Опции:"
    }

    msg = bot.send_message(message.chat.id, text=text[language])
    bot.register_next_step_handler(msg, partial(get_additional_options, bot=bot, language=language, car=car))


def get_additional_options(message, bot: TeleBot, car: Car, language: str):
    car.additional_options = message.text
    set_additional_options(car.id, message.text)

    text = {
        UZBEK_LANGUAGE: f"""🔥{car.model}-{car.price}🔥

▪️Avtomobil modeli va markasi: {car.model}
▪️Narxi: {car.price}
▪️Kuzov turi: {car.body_type}
▪️Ishlab chiqarilgan yili: {car.issue_year}
▪️️Yurgan masofasi: {car.mileage}
▪️Uzatmalar qutisi: {car.gearbox_type}
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


def handle_body_type(bot: TeleBot, callback: types.CallbackQuery):
    user = get_user_by_chat_id(callback.message.chat.id)
    car = get_last_car_by_user_id(user.id)

    if callback.data == CALLBACK_DATA_BODY_TYPE_OTHER:
        text = {
            UZBEK_LANGUAGE: "Kuzov turi:",
            RUSSIAN_LANGUAGE: "Тип кузова:"
        }

        msg = bot.send_message(callback.message.chat.id, text=text[user.language])
        bot.register_next_step_handler(msg, partial(get_body_type, bot=bot, language=user.language, car=car))
    else:
        car.body_type = body_type[callback.data][user.language]
        set_body_type(car.id, car.body_type)

        text = {
            UZBEK_LANGUAGE: 'Kilometr:',
            RUSSIAN_LANGUAGE: "Пробег:"
        }

        msg = bot.send_message(callback.message.chat.id, text=text[user.language])
        bot.register_next_step_handler(msg, partial(get_mileage, bot=bot, language=user.language, car=car))


def handle_gearbox_type(bot: TeleBot, callback: types.CallbackQuery):
    user = get_user_by_chat_id(callback.message.chat.id)
    car = get_last_car_by_user_id(user.id)

    if callback.data == CALLBACK_DATA_GEARBOX_TYPE_OTHER:
        text = {
            UZBEK_LANGUAGE: 'Uzatmalar qutisi:',
            RUSSIAN_LANGUAGE: "Тип коробки передач:"
        }

        msg = bot.send_message(callback.message.chat.id, text=text[user.language])
        bot.register_next_step_handler(msg, partial(get_gearbox_type, bot=bot, language=user.language, car=car))
    else:
        car.gearbox_type = gearbox_type[callback.data][user.language]
        set_gearbox_type(car.id, car.gearbox_type)

        text = {
            UZBEK_LANGUAGE: 'Chiqarilgan yili:',
            RUSSIAN_LANGUAGE: "Год выпуска:"
        }

        msg = bot.send_message(callback.message.chat.id, text=text[user.language])
        bot.register_next_step_handler(msg, partial(get_issue_year, bot=bot, language=user.language, car=car))


def handle_color(bot: TeleBot, callback: types.CallbackQuery):
    user = get_user_by_chat_id(callback.message.chat.id)
    car = get_last_car_by_user_id(user.id)

    if callback.data == CALLBACK_DATA_COLOR_OTHER:
        text = {
            UZBEK_LANGUAGE: 'Rang:',
            RUSSIAN_LANGUAGE: "Цвет:"
        }

        msg = bot.send_message(callback.message.chat.id, text=text[user.language])
        bot.register_next_step_handler(msg, partial(get_color, bot=bot, language=user.language, car=car))
    else:
        car.color = color[callback.data][user.language]
        set_color(car.id, car.color)

        text = {
            UZBEK_LANGUAGE: 'Dvigatel hajmi:',
            RUSSIAN_LANGUAGE: "Объем двигателя:"
        }

        msg = bot.send_message(callback.message.chat.id, text=text[user.language])
        bot.register_next_step_handler(msg, partial(get_engine_capacity, bot=bot, language=user.language, car=car))


def handle_fuel_type(bot: TeleBot, callback: types.CallbackQuery):
    user = get_user_by_chat_id(callback.message.chat.id)
    car = get_last_car_by_user_id(user.id)

    car.fuel_type = fuel_type[callback.data][user.language]
    set_fuel_type(car.id, car.fuel_type)

    markup = types.InlineKeyboardMarkup()
    excellent = types.InlineKeyboardButton(machine_condition[CALLBACK_DATA_MACHINE_CONDITION_EXCELLENT][user.language],
                                           callback_data=CALLBACK_DATA_MACHINE_CONDITION_EXCELLENT)
    good = types.InlineKeyboardButton(machine_condition[CALLBACK_DATA_MACHINE_CONDITION_GOOD][user.language],
                                      callback_data=CALLBACK_DATA_MACHINE_CONDITION_GOOD)
    average = types.InlineKeyboardButton(machine_condition[CALLBACK_DATA_MACHINE_CONDITION_AVERAGE][user.language],
                                         callback_data=CALLBACK_DATA_MACHINE_CONDITION_AVERAGE)
    needs_repair = types.InlineKeyboardButton(
        machine_condition[CALLBACK_DATA_MACHINE_CONDITION_NEEDS_REPAIR][user.language],
        callback_data=CALLBACK_DATA_MACHINE_CONDITION_NEEDS_REPAIR)
    markup.add(excellent, good, average, needs_repair)

    text = {
        UZBEK_LANGUAGE: 'Avtomobil holati:',
        RUSSIAN_LANGUAGE: "Состояние машины:"
    }

    bot.send_message(callback.message.chat.id, text=text[user.language], reply_markup=markup)


def handle_machine_condition(bot: TeleBot, callback: types.CallbackQuery):
    user = get_user_by_chat_id(callback.message.chat.id)
    car = get_last_car_by_user_id(user.id)

    car.machine_condition = machine_condition[callback.data][user.language]
    set_machine_condition(car.id, car.machine_condition)

    markup = types.InlineKeyboardMarkup()
    one = types.InlineKeyboardButton(number_of_owners[CALLBACK_DATA_NUMBER_OF_OWNERS_1][user.language],
                                     callback_data=CALLBACK_DATA_NUMBER_OF_OWNERS_1)
    two = types.InlineKeyboardButton(number_of_owners[CALLBACK_DATA_NUMBER_OF_OWNERS_2][user.language],
                                     callback_data=CALLBACK_DATA_NUMBER_OF_OWNERS_2)
    three = types.InlineKeyboardButton(number_of_owners[CALLBACK_DATA_NUMBER_OF_OWNERS_3][user.language],
                                       callback_data=CALLBACK_DATA_NUMBER_OF_OWNERS_3)
    other = types.InlineKeyboardButton(number_of_owners[CALLBACK_DATA_NUMBER_OF_OWNERS_OTHER][user.language],
                                       callback_data=CALLBACK_DATA_NUMBER_OF_OWNERS_OTHER)
    markup.add(one, two, three, other)

    text = {
        UZBEK_LANGUAGE: 'Egalari soni:',
        RUSSIAN_LANGUAGE: "Количество владельцев:"
    }

    bot.send_message(callback.message.chat.id, text=text[user.language], reply_markup=markup)


def handle_number_of_owners(bot: TeleBot, callback: types.CallbackQuery):
    user = get_user_by_chat_id(callback.message.chat.id)
    car = get_last_car_by_user_id(user.id)

    if callback.data == CALLBACK_DATA_NUMBER_OF_OWNERS_OTHER:
        text = {
            UZBEK_LANGUAGE: 'Egalari soni:',
            RUSSIAN_LANGUAGE: "Количество владельцев:"
        }

        msg = bot.send_message(callback.message.chat.id, text=text[user.language])
        bot.register_next_step_handler(msg, partial(get_number_of_owners, bot=bot, language=user.language, car=car))
    else:
        car.number_of_owners = number_of_owners[callback.data][user.language]
        set_number_of_owners(car.id, car.number_of_owners)

        text = {
            UZBEK_LANGUAGE: 'Aloqa telefon raqami:',
            RUSSIAN_LANGUAGE: "Телефон для связи:"
        }

        msg = bot.send_message(callback.message.chat.id, text=text[user.language])
        bot.register_next_step_handler(msg, partial(get_phone_number, bot=bot, language=user.language, car=car))


def handle_city(bot: TeleBot, callback: types.CallbackQuery):
    user = get_user_by_chat_id(callback.message.chat.id)
    car = get_last_car_by_user_id(user.id)

    if callback.data == CALLBACK_DATA_CITY_OTHER:
        text = {
            UZBEK_LANGUAGE: 'Shahar:',
            RUSSIAN_LANGUAGE: "Город:"
        }

        msg = bot.send_message(callback.message.chat.id, text=text[user.language])
        bot.register_next_step_handler(msg, partial(get_city, bot=bot, language=user.language, car=car))
    else:
        car.city = city[callback.data][user.language]
        set_city(car.id, car.city)

        markup = types.InlineKeyboardMarkup()
        cash = types.InlineKeyboardButton(payment_types[CALLBACK_DATA_PAYMENT_TYPE_CASH][user.language],
                                          callback_data=CALLBACK_DATA_PAYMENT_TYPE_CASH)
        leasing = types.InlineKeyboardButton(payment_types[CALLBACK_DATA_PAYMENT_TYPE_LEASING][user.language],
                                             callback_data=CALLBACK_DATA_PAYMENT_TYPE_LEASING)
        transfer = types.InlineKeyboardButton(payment_types[CALLBACK_DATA_PAYMENT_TYPE_TRANSFER][user.language],
                                              callback_data=CALLBACK_DATA_PAYMENT_TYPE_TRANSFER)
        credit = types.InlineKeyboardButton(payment_types[CALLBACK_DATA_PAYMENT_TYPE_CREDIT][user.language],
                                            callback_data=CALLBACK_DATA_PAYMENT_TYPE_CREDIT)
        installment = types.InlineKeyboardButton(payment_types[CALLBACK_DATA_PAYMENT_TYPE_INSTALLMENT][user.language],
                                                 callback_data=CALLBACK_DATA_PAYMENT_TYPE_INSTALLMENT)
        markup.add(cash, leasing, transfer, credit, installment)

        text = {
            UZBEK_LANGUAGE: "To'lov turi:",
            RUSSIAN_LANGUAGE: "Выберете вид оплаты, доступны такие виды как (Наличка/Кредит/Лизинг/Рассрочка):"
        }

        bot.send_message(callback.message.chat.id, text=text[user.language], reply_markup=markup)


def handle_payment_type(bot: TeleBot, callback: types.CallbackQuery):
    user = get_user_by_chat_id(callback.message.chat.id)
    car = get_last_car_by_user_id(user.id)

    car.payment_type = payment_types[callback.data][user.language]
    set_payment_type(car.id, car.payment_type)

    text = {
        UZBEK_LANGUAGE: "Qo'shimcha variantlar:",
        RUSSIAN_LANGUAGE: "Доп. Опции:"
    }

    msg = bot.send_message(callback.message.chat.id, text=text[user.language])
    bot.register_next_step_handler(msg, partial(get_additional_options, bot=bot, language=user.language, car=car))
