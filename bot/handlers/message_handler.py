from telebot import TeleBot

def register_message_handlers(bot: TeleBot):
    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        bot.reply_to(message, "You sent a text message!")
