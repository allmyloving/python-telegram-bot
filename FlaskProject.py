import requests, json
from flask import Flask, request, jsonify, current_app

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
    data = json.loads(request.data)
    print(
        "New commit by: {}".format(data['commits'][0]['author']['name']))
    return "OK"


@app.route('/bot')
def call_bot():
    req = requests.get(URL + "setWebhook?url=%s" % APP_URL)
    print(req.status_code)
    return req.status_code == 200


if call_bot():
    print("all ok")

if __name__ == '__main__':
    app.run()
    if call_bot():
        print("All ok")
