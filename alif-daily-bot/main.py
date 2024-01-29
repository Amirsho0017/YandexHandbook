import locale
from datetime import datetime

import telebot
from telebot import custom_filters
from telebot.handler_backends import StatesGroup, State
from telebot.storage import StateMemoryStorage

from config import daily_bot_token, daily_chat_id, admin_chat_id, general_group_id, manager_chat_id
from db import conn as connection

locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
state_storage = StateMemoryStorage()
bot = telebot.TeleBot(daily_bot_token, state_storage=state_storage)


class ReportState(StatesGroup):
    last_work_day = State()
    today = State()
    difficulties = State()


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


@bot.message_handler(commands=['start'], chat_types=['private'])
@check_is_reported
def start(message):
    user_id = message.from_user.id
    if check_user(user_id):
        welcome_message = '''Привеееет 👋, Я Алиф Дейли Бот💚\nПожалуйста, ответьте на следующие вопросы: \n'''
        bot.send_message(message.chat.id, welcome_message)
        bot.set_state(user_id, ReportState.last_work_day, message.chat.id)
        bot.send_message(user_id, "Чем занимались вчера?")

    else:
        admin = f'<b><a href=\"tg://user?id={admin_chat_id}\">{"Admin"}</a></b>'
        bot.send_message(user_id, f"Вас нету в списке юзеров, попросите {admin} добавить вас)", parse_mode="HTML")
        bot.send_message(user_id, f"Для этоreportsго отправьте админу ваш айди: {user_id}")


@bot.message_handler(state="*", commands=['cancel'])
def any_state(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(telebot.types.KeyboardButton('/start'))
    bot.send_message(message.chat.id, "Ваши ответы удалены, для запуска нажмите /start.",
                     reply_markup=markup)
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(state="*", commands=['send'])
def send_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(telebot.types.KeyboardButton('/start'))
    current_date = datetime.now()
    formatted_table = format_responses(message)
    formatted_date = current_date.strftime("%A, %d %B %Y")
    user_name_link = f'<b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a></b>'

    report_text = f'''Ежедневный отчет от {user_name_link}\n{formatted_date}
                           {formatted_table}'''

    bot.send_message(daily_chat_id, report_text, parse_mode='HTML')

    bot.send_message(message.from_user.id, "Ваши ответы отправлены в нужную группу. \nПродуктивного дня Вам.",
                     reply_markup=markup)

    with bot.retrieve_data(message.from_user.id, message.chat.id) as response:
        forwardDifficulties(response['difficulties'], user_name_link)

    bot.delete_state(message.from_user.id, message.chat.id)


def forwardDifficulties(text, user_name_link):
    manager_info = bot.get_chat(manager_chat_id)
    manager_name_link = f'<b><a href="tg://user?id={manager_chat_id}">{manager_info.first_name}</a></b>'

    if text in ('Нету сложностей', 'Никаких', 'Нету', '-'):
        pass
    else:
        separator = "——————————————————————"
        bot.send_message(general_group_id,
                         f"Y {user_name_link} возникли следующие сложности: \n "
                         f"{separator}\n {text}"
                         f"\n{separator}\n"
                         f"Аки {manager_name_link} нуждемся в вашей помощи",
                         parse_mode='HTML')


@bot.message_handler(state=ReportState.last_work_day)
def last_work_day_get(message):
    bot.send_message(message.chat.id, 'Чем будете заниматься сегодня?')
    bot.set_state(message.from_user.id, ReportState.today, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['last_work_day'] = message.text
        print(data)


@bot.message_handler(state=ReportState.today)
def last_work_day_get(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(telebot.types.KeyboardButton('Нету сложностей'))
    bot.send_message(message.chat.id, 'Какие сложности возникли?', reply_markup=markup)
    bot.set_state(message.from_user.id, ReportState.difficulties, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['today'] = message.text


@bot.message_handler(state=ReportState.difficulties)
def difficulties_get(message):
    commands = {'Изменить запись': '/cancel', 'Отправить в нужную группу': '/send'}
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    for key, val in commands.items():
        markup.add(telebot.types.KeyboardButton(val), row_width=2)

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['difficulties'] = message.text

    current_date = datetime.now()
    formatted_table = format_responses(message)
    formatted_date = current_date.strftime("%A, %d %B %Y")
    user_name_link = f'<b><a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a></b>'

    report_text = f'''Ежедневный отчет от {user_name_link}\n{formatted_date}
                       {formatted_table}'''
    bot.send_message(message.from_user.id, f"Вот так выглядит ваши ответы: \n{report_text}", reply_markup=markup,
                     parse_mode='HTML')


def format_responses(message):
    separator = "——————————————————————"

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        formatted_string = f"\n{separator}\nВчера:\n    " + "\n    ".join(data['last_work_day'].splitlines()) + \
                           f"\n\n{separator}\nСегодня:\n    " + "\n    ".join(data['today'].splitlines()) + \
                           f"\n\n{separator}\nСложности:\n    " + "\n    ".join(data['difficulties'].splitlines()) + \
                           f"\n{separator}"
    return formatted_string


bot.add_custom_filter(custom_filters.StateFilter(bot))

if __name__ == "__main__":
    bot.infinity_polling()
