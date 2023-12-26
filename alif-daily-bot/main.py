import telebot

from config import daily_bot_token

bot = telebot.TeleBot(daily_bot_token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message, message.text
    )


if __name__ == "__main__":
    bot.polling()
