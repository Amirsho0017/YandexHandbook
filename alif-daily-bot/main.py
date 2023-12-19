#!/usr/bin/python
import telebot

API_TOKEN = '6284285588:AAFMzKqT3jvcqvTQ4RfuTgchXqDOkByBkHA'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Привеееет 👋, Я Алиф Дейли Бот💚.
Я хочу повысить вашу продуктивность. Для этого ответьте, пожалуйста, на следующие вопросы.\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.polling()
