from time import sleep

import requests
from flask import Flask

app = Flask(__name__)

TOKEN = '260039213:AAHHKne9Sme8r-fROdHRBk577_o7XZblBcQ'
URL = "https://api.telegram.org/bot%s/" % TOKEN
APP_URL = "https://morning-fortress-78667.herokuapp.com/"


def main():
    update_id = last_update(get_updates_json(URL))['update_id']
    while True:
        if update_id == last_update(get_updates_json(URL))['update_id']:
            send_mess(get_chat_id(last_update(get_updates_json(URL))), 'test')
            update_id += 1
            sleep(1)


if __name__ == '__main__':
    main()


def get_updates_json(request):
    params = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()


def last_update(data):
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id


def send_mess(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(URL + 'sendMessage', data=params)
    return response

#
# COMMANDS = {"/start": start,
#             "/help": help_comm,
#             "/benice": be_nice,
#             "/addrem": add_rem}
NICE_MSG = ["You look great today!",
            "You're gonna be fine!",
            "Love and peace",
            "Keep calm and learn Java ~~~~"]
