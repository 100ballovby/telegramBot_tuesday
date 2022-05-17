import telebot
import requests as r


def get_currencies():
    url_codes = 'https://api.coinbase.com/v2/currencies'
    response_code = r.get(url_codes)
    data = response_code.json()
    currencies = {}
    for cur in data['data']:
        currencies[cur['id']] = cur['name']

    return currencies


def get_rates(base, amount, target):
    url_codes = f'https://api.coinbase.com/v2/exchange-rates?currency={base.upper()}'
    try:
        response_code = r.get(url_codes)
        data = response_code.json()
        rates = data['data']['rates']
        result = round(amount * float(rates[target.upper()]), 2)
        return result
    except:
        return None

bot = telebot.TeleBot('5140891289:AAEx2yvu5IuypNxo-QOVnhipr99P5yrhySg')


@bot.message_handler(commands=['start'])  # что делаем, когда отправили /start
def start_message(message):
    with open('assets/greeting.txt', encoding='utf8') as file:
        greeting = file.read()
    bot.send_message(message.chat.id, greeting)


@bot.message_handler(commands=['help'])  # что делаем, когда отправили /start
def help_message(message):
    with open('assets/help.txt', encoding='utf8') as file:
        help_text = file.read()
    bot.send_message(message.chat.id, help_text)


@bot.message_handler(content_types=['text'])
def get_codes(message):
    codes = get_currencies()
    if message.text.startswith('/cur_code'):  # если текст сообщения начинается с /cur_code
        try:
            user_message = message.text.split()  # превратить сообщение пользователя в список
            answer = user_message[1].upper() in codes.keys()
            bot.send_message(message.chat.id, codes[user_message[1].upper()])
        except (ValueError, TypeError, IndexError, SyntaxError, KeyError):
            bot.send_message(message.chat.id, 'Такой валюты нет!')



bot.polling(none_stop=True, interval=0)
