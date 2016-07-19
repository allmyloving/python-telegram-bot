import requests
import logging
from flask import Flask
from flask import request

app = Flask(__name__)

TOKEN = '260039213:AAHHKne9Sme8r-fROdHRBk577_o7XZblBcQ'
URL = "https://api.telegram.org/bot%s/" % TOKEN
APP_URL = "http://localhost:5000"


@app.route('/hello')
def hello_world():
    return 'Hello World!'


@app.route('/', methods=['GET', 'POST'])
def main():
    print("Main function called")
    print("Request type: " + request.method)
    print("Request url: ", request.url)
    return ""


def call_bot():
    hook = requests.get(URL + "setWebhook?url=%s" % APP_URL).content
    print(hook)
    return hook.status == '200'


if __name__ == '__main__':
    app.run()
    if call_bot():
        print("All ok")
