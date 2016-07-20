import requests
import json
import random
from flask import Flask, request
from dbmanager import main

app = Flask(__name__)

TOKEN = '260039213:AAHHKne9Sme8r-fROdHRBk577_o7XZblBcQ'
URL = "https://api.telegram.org/bot%s/" % TOKEN
APP_URL = "https://morning-fortress-78667.herokuapp.com/"


@app.route('/hello')
def hello_world():
    return 'Hello World!'


@app.route('/', methods=['POST'])
def main():
    update = json.loads(request.data)
    print(update)
    print(update['message'].get('text'))
    message = update['message']

    response = execute_comm(message.get('text'), message)
    print(response)
    send_response(response, message['chat']['id'])
    return "OK"


def execute_comm(command, message):
    comm = COMMANDS.get(message.get('text'))
    if comm is None:
        return "Error, command %s not found" % command
    return comm(message)


def send_response(response, chat_id):
    data = {'chat_id': chat_id,
            'text': response}
    requests.post(URL + "sendMessage", data)


def start(message):
    return "Hello there %s!" % get_user_name(message)


def help_comm(message):
    # response = {'chat_id': message['chat']['id']}
    result = ["Hello %s! \r\nI can accept only these commands:\r\n" % get_user_name(message)]
    for cmd in COMMANDS:
        result.append(cmd)
    return "\n\t".join(result)


def be_nice(message):
    index = random.randint(0, len(NICE_MSG) - 1)
    return NICE_MSG[index]


def add_rem(message):
    main()
    return 'completed'


def get_user_name(message):
    return message['from'].get('first_name')


@app.route('/bot')
def call_bot():
    req = requests.get(URL + "setWebhook?url=%s" % APP_URL)
    print(req.status_code)
    return req.status_code == 200


if call_bot():
    print("all ok")

COMMANDS = {"/start": start,
            "/help": help_comm,
            "/benice": be_nice,
            "/addrem": add_rem}
NICE_MSG = ["You look great today!",
            "You're gonna be fine!",
            "Love and peace",
            "Keep calm and learn Java ~~~~"]

if __name__ == '__main__':
    app.run()
    if call_bot():
        print("All ok")
