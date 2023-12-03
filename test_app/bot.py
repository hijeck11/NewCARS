import os
from telebot import TeleBot

TELEGRAM_BOT_TOKEN = '6887121770:AAFQCwb0tTDi4ReHoSlZsd5xEqkfvkHKtq8'
TELEGRAM_CHAT_ID = '645247611'


bot = TeleBot((TELEGRAM_BOT_TOKEN), threaded=False)


def bot_save():
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text='Заказана новая машина')


def bot_delete():
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text='Были удалены данные')
