import os

import emoji
import telebot
from loguru import logger

from src.utils.constant import keyboards
from src.utils.io import write_json


class But:
    """
    telegram bot to randomly connect two strangers
    """
    def __init__(self):
        self.bot = telebot.TeleBot(os.environ['BOT_TOKEN'])
        self.echo = self.bot.message_handler(func=lambda m: True)(self.echo_all)

    def run(self):
        logger.info('bot is running...')
        self.bot.infinity_polling()
    
    def echo_all(self, message):
        print(emoji.demojize(message.text))
        self.bot.send_message(message.chat.id, message.text, reply_markup=keyboards.main)
        write_json(message.json, 'message.json')

if __name__=='__main__':
    bot = But()
    bot.run()

