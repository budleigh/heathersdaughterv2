import datetime
from peewee import *

database = SqliteDatabase('hd.db')

class Order(Model):
    name = CharField()
    instructions = TextField()
    counts = TextField()
    created = DateTimeField(default=datetime.datetime.now)