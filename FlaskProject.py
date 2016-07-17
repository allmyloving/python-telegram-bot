import requests
from flask import Flask

TOKEN = '260039213:AAHHKne9Sme8r-fROdHRBk577_o7XZblBcQ'
URL = "https://api.telegram.org/bot%s/" % TOKEN
APP_URL = "http://localhost:5000"
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/bot')
def call_bot():
    return requests.get(URL + "setWebhook?url=%s" % APP_URL).content


if __name__ == '__main__':
    app.run()
