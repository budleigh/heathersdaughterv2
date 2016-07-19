import os
from pymongo import MongoClient

client = MongoClient(os.environ.get('MONGODB_URI', 'localhost'))
db = client.db
col = db.col


def save_order(order):
    try:
        col.insert_one(order)
        return True
    except:
        return False


def get_orders():
    return col.find()