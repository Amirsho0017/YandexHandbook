import locale
from datetime import datetime

import telebot
from tabulate import tabulate

from config import daily_bot_token, daily_chat_id

locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
bot = telebot.TeleBot(daily_bot_token)

user_responses = {}


@bot.message_handler(commands=['start'], chat_types=['private'])
def start(message):
    user_id = message.from_user.id
    user_responses[user_id] = []
    welcome_message = '''Привеееет 👋, Я Алиф Дейли Бот💚
Пожалуйста, ответьте на следующие вопросы: \n'''

    bot.send_message(message.chat.id, welcome_message)
    bot.send_message(user_id, "Чем занимались вчера?")
    user_responses[user_id].append('started')


@bot.message_handler(func=lambda message: True, chat_types=['private'])
def handle_user_response(message):
    user_id = message.from_user.id
    response = message.text
    user_responses[user_id].append(response)
    current_date = datetime.now()
    formatted_date = current_date.strftime("%A, %d %B %Y")

    user_name_link = f'<b><a href="tg://user?id={user_id}">{message.from_user.first_name}</a></b>'

    if len(user_responses[user_id]) == 2 and 'started' in user_responses[user_id]:
        bot.send_message(user_id, "Чем будете заниматься сегодня?")
    elif len(user_responses[user_id]) == 3 and 'started' in user_responses[user_id]:
        bot.send_message(user_id, "Какие сложности возникли?")
    elif len(user_responses[user_id]) == 4 and 'started' in user_responses[user_id]:
        bot.send_message(user_id, "Ваши ответы отправлены в нужную группу. \nПродуктивного дня Вам.🥰")
        formatted_table = format_responses(user_responses[user_id])
        report_text = f'''Ежедневный отчет от {user_name_link}\n{formatted_date}
        {formatted_table}'''

        bot.send_message(daily_chat_id, report_text, parse_mode='HTML')
        user_responses[user_id].clear()
    else:
        bot.send_message(message.chat.id, 'На сегодня хватит, пага биеен бо)')


def format_responses(responses):
    separator = "—————————————————————————————"

    formatted_string = f"\n{separator}\nВчера:\n    " + "\n    ".join(responses[1].splitlines()) + \
                       f"\n\n{separator}\nСегодня:\n    " + "\n    ".join(responses[2].splitlines()) + \
                       f"\n\n{separator}\nСложности:\n    " + "\n    ".join(responses[3].splitlines()) + \
                       f"\n{separator}"
    return formatted_string


@bot.message_handler(commands=['my_id'], chat_types=['private'])
def get_user_id(message):
    bot.reply_to(message, message.from_user.id)


@bot.message_handler(commands=['chat_id'])
def get_chat_id(message):
    bot.reply_to(message, message.chat.id)


def get_questions():
    headers = ['Вопросы']
    questions = [
        ['1)', 'Чем Вы занимались вчера?'],
        ['2)', 'Чем будете заниматься сегодня?'],
        ['3)', 'Какие сложности есть?']
    ]
    table = tabulate(questions, headers)
    return f'{table}'


if __name__ == "__main__":
    bot.polling()
