import telebot
from random import *

bot = telebot.TeleBot('7044491469:AAGAap6-WV4ed0y7MjKmVDHDmYpCP9Ar0r8')


answer = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name}</b> <b>{message.from_user.last_name}</b>, я магический шар и я знаю ответ на любой твой вопрос!!!'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler()
def get_user_text(message):
    if message.text:
        bot.send_message(message.chat.id, {choice(answer)}, parse_mode='html')


bot.polling(none_stop=True)






