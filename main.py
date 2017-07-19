import random

import requests
import telebot
from flask import Flask

import dbmanager

app = Flask(__name__)

TOKEN = '260039213:AAHHKne9Sme8r-fROdHRBk577_o7XZblBcQ'
URL = "https://api.telegram.org/bot%s/" % TOKEN
# APP_URL = "https://morning-fortress-78667.herokuapp.com/"

bot = telebot.TeleBot(TOKEN)

COMMANDS = ["/start", "/help", "/benice", "/addrem"]
NICE_MSG = ["You look great today!",
            "You're gonna be fine!",
            "Love and peace",
            "Keep calm and learn Java ~~~~"]


@app.route('/hello')
def hello_world():
    return 'Hello World!'


def send_response(response, chat_id):
    data = {'chat_id': chat_id,
            'text': response}
    requests.post(URL + "sendMessage", data)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello there %s!" % get_user_name(message))


@bot.message_handler(commands=['help'])
def help_comm(message):
    # response = {'chat_id': message['chat']['id']}
    result = ["Hello %s! \r\nI can accept only these commands:\r\n" % get_user_name(message)]
    for cmd in COMMANDS:
        result.append(cmd)
    bot.reply_to(message, "\n\t".join(result))


@bot.message_handler(commands=['be_nice'])
def be_nice(message):
    index = random.randint(0, len(NICE_MSG) - 1)
    bot.reply_to(message, NICE_MSG[index])


@bot.message_handler(commands=['addrem'])
def add_rem(message):
    dbmanager.add(message)
    bot.reply_to(message, 'completed')


def get_user_name(message):
    return message['from'].get('first_name')


@app.route('/bot')
def call_bot():
    req = requests.post(URL + "setWebhook?url=%s" % '')
    print(req.status_code)
    return req.status_code == 200

call_bot()
bot.polling(none_stop=True)
