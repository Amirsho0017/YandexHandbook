import locale
from datetime import datetime

import telebot

from config import daily_bot_token, daily_chat_id, admin_chat_id
from db import conn as connection

locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
bot = telebot.TeleBot(daily_bot_token)

user_responses = {}
cursor = connection.cursor()


def set_report(user_id):
    try:
        with connection as conn:
            with conn.cursor() as cursor:
                cursor.execute('INSERT INTO reports (user_id) VALUES (%s)', (str(user_id),))
                conn.commit()

    except Exception as e:
        print(f"Error: {e}")


def get_users():
    cursor.execute('Select user_id from users')
    result_list = [item[0] for item in cursor.fetchall()]

    return result_list


def check_is_reported(f):
    def reported_today(message):
        cursor.execute('SELECT date FROM reports WHERE user_id = %s ORDER BY date DESC LIMIT 1',
                       (str(message.from_user.id),))
        result = cursor.fetchone()

        if result is not None and result[0] == datetime.now().date():
            bot.send_message(message.from_user.id, 'Сегодня вы уже сдавали отчет, басай имрузайшда)')
        else:
            f(message)

    return reported_today


def check_user(user_id):
    if str(user_id) in get_users():
        return True
    else:
        return False


@bot.message_handler(commands=['my_id'], chat_types=['private'])
def get_user_id(message):
    bot.reply_to(message, message.from_user.id)


@bot.message_handler(commands=['chat_id'])
def get_chat_id(message):
    bot.reply_to(message, message.chat.id)

@bot.message_handler(commands=['start'], chat_types=['private'])
@check_is_reported
def start(message):
    user_id = message.from_user.id
    if check_user(user_id):
        user_responses[user_id] = []
        welcome_message = '''Привеееет 👋, Я Алиф Дейли Бот💚\nПожалуйста, ответьте на следующие вопросы: \n'''
        bot.send_message(message.chat.id, welcome_message)
        bot.send_message(user_id, "Чем занимались вчера?")
    else:
        admin = f'<b><a href=\"tg://user?id={admin_chat_id}\">{"Admin"}</a></b>'
        bot.send_message(user_id, f"Вас нету в списке юзеров, попросите {admin} добавить вас)", parse_mode="HTML")
        bot.send_message(user_id, f"Для этоreportsго отправьте админу ваш айди: {user_id}")


@bot.message_handler(func=lambda message: check_user(message.from_user.id), chat_types=['private'])
@check_is_reported
def handle_user_response(message):
    user_id = message.from_user.id
    response = message.text
    current_date = datetime.now()
    user_responses[user_id].append(response)
    formatted_date = current_date.strftime("%A, %d %B %Y")
    user_name_link = f'<b><a href="tg://user?id={user_id}">{message.from_user.first_name}</a></b>'

    if len(user_responses[user_id]) == 1:
        bot.send_message(user_id, "Чем будете заниматься сегодня?")
    elif len(user_responses[user_id]) == 2:
        bot.send_message(user_id, "Какие сложности возникли?")
    elif len(user_responses[user_id]) == 3:
        bot.send_message(user_id, "Ваши ответы отправлены в нужную группу. \nПродуктивного дня Вам.")
        formatted_table = format_responses(user_responses[user_id])
        report_text = f'''Ежедневный отчет от {user_name_link}\n{formatted_date}
                {formatted_table}'''
        bot.send_message(daily_chat_id, report_text, parse_mode='HTML')
        user_responses[user_id].clear()
        set_report(user_id)
    else:
        bot.send_message(message.chat.id, 'На сегодня хватит, пага биеен бо)')


#


def format_responses(responses):
    separator = "—————————————————————————————"

    formatted_string = f"\n{separator}\nВчера:\n    " + "\n    ".join(responses[0].splitlines()) + \
                       f"\n\n{separator}\nСегодня:\n    " + "\n    ".join(responses[1].splitlines()) + \
                       f"\n\n{separator}\nСложности:\n    " + "\n    ".join(responses[2].splitlines()) + \
                       f"\n{separator}"
    return formatted_string


if __name__ == "__main__":
    bot.infinity_polling()
