import os
from telebot import TeleBot

TOKEN = os.getenv('TOKEN')
bot = TeleBot(TOKEN)
bot.remove_webhook()
bot.set_webhook(f"{os.getenv('APP_URL')}/{TOKEN}")


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Hi, I am ready for work! I will echo any text you send me!")


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)
