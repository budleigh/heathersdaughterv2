import os
from pymongo import MongoClient

client = MongoClient(os.environ.get('MONGODB_URI', 'localhost'))
db = client.db
col = db.col


def save_order(order):
    col.insert_one(order)


def get_orders():
    for order in col.find({}):
        yield order