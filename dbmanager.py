from pymongo import MongoClient

DB_URL = "mongodb://admin:admin@ds023325.mlab.com:23325/heroku_drc033gr"


def add():
    client = MongoClient(DB_URL)
    db = client.heroku_drc033gr
    result = db.rem.insert_one({
        'chat_id': '123',
        'time': '1111',
        'text': 'reminder'
    })
    print(result.inserted_id)
