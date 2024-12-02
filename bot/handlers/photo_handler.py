from telebot import TeleBot, types

from config import UZBEK_LANGUAGE, RUSSIAN_LANGUAGE
from bot.models.user import *
from bot.repository.user import get_user_by_chat_id
from bot.repository.car import *
from bot.repository.tariff import *
import config

import os
from werkzeug.utils import secure_filename


def register_photo_handlers(bot: TeleBot):
    @bot.message_handler(content_types=['photo'])
    def handle_photo(message):
        upload_folder = "bot/uploads/"

        file_info = bot.get_file(message.photo[-1].file_id)
        file_path = file_info.file_path
        local_photo_path = os.path.join(upload_folder, f"{secure_filename(file_info.file_id)}.jpg")
        downloaded_file = bot.download_file(file_path)  # Only one argument, file_path

        with open(local_photo_path, 'wb') as f:
            f.write(downloaded_file)  # Write the content to the file

        user = get_user_by_chat_id(message.chat.id)
        car = get_last_car_by_user_id(user.id)
        add_car_photo(car.id, local_photo_path)

        count = get_photo_count(car.id)

        if count >= 6:
            text = {
                UZBEK_LANGUAGE: f'Клиент ознакомился с планом\n\nЮзернейм: @{message.from_user.username}',
                RUSSIAN_LANGUAGE: f'Клиент ознакомился с планом\n\nЮзернейм: @{message.from_user.username}'
            }
            bot.send_message(config.ADMIN_CHAT_ID, text=text[user.language])

            text = "Tarif rejasini tanlang: \n\n"
            if user.language == RUSSIAN_LANGUAGE:
                text = "Пожалуйста выберите тарифный план: \n\n"

            markup = types.InlineKeyboardMarkup()
            tariffs = get_tariffs()
            for tariff in tariffs:
                tariff_detail = get_translation(tariff.id, user.language)
                markup.add(types.InlineKeyboardButton(tariff_detail.name, callback_data=tariff.callback_data))

                text = f"""{text}{tariff.amount} - "{tariff_detail.name}" tarifi\n● {tariff_detail.description}\n\n"""

            bot.send_message(message.chat.id, text=text, reply_markup=markup)
