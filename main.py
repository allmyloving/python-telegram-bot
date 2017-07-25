import telebot
from flask import Flask, request

app = Flask(__name__)

TOKEN = '260039213:AAHHKne9Sme8r-fROdHRBk577_o7XZblBcQ'
URL = "https://api.telegram.org/bot%s/" % TOKEN
# APP_URL = "https://morning-fortress-78667.herokuapp.com/"

bot = telebot.TeleBot(TOKEN)
bot.remove_webhook()
bot.set_webhook(URL)

COMMANDS = ["/start", "/help", "/benice", "/addrem"]
NICE_MSG = ["You look great today!",
            "You're gonna be fine!",
            "Love and peace",
            "Keep calm and learn Java ~~~~"]


@app.route('/{}'.format(TOKEN), methods=["POST"])
def lololo():
    update = request.get_json()
    if "message" in update:
        text = update["message"]["text"]
        chat_id = update["message"]["chat"]["id"]
        bot.send_message(chat_id, "you said '{}'".format(text))
    return "ok"


if __name__ == '__main__':
    app.run()
