from telebot import types
from bot.repository.user import *
from const import *


def handle_russian(bot, callback, chat_id=None):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Дать рекламное обьявление🛍",
                                          callback_data=CALLBACK_DATA_ADD_ADVERTISEMENT))
    markup.add(types.InlineKeyboardButton("Нужна помощь с другим вопросом❓",
                                          callback_data=CALLBACK_DATA_GIVE_QUESTION))

    user = get_user_by_chat_id(chat_id or callback.message.chat.id)
    set_language(user, CALLBACK_DATA_RU)

    bot.send_message(chat_id or callback.message.chat.id,
                     "Подскажите, пожалуйста, с чем связан ваш вопрос?",
                     reply_markup=markup)


def handle_uzbek(bot, callback, chat_id=None):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Reklama berish🛍",
                                          callback_data=CALLBACK_DATA_ADD_ADVERTISEMENT))
    markup.add(types.InlineKeyboardButton("Boshqa savol bo'yicha yordam kerak❓",
                                          callback_data=CALLBACK_DATA_GIVE_QUESTION))

    user = get_user_by_chat_id(chat_id or callback.message.chat.id)
    set_language(user, CALLBACK_DATA_UZ)

    bot.send_message(chat_id or callback.message.chat.id,
                     "Aytingchi, sizning savolingiz nima bilan bog'liq?",
                     reply_markup=markup)
