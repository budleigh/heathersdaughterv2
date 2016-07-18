import datetime
import os
from peewee import *

db_url = os.environ.get(
    'DATABASE_URL', 
    'postgres://yoozer:Generalkdrama1{}@localhost:5432/hdtest'
)


class BaseModel(Model):

    class Meta:
        database = database


class Order(BaseModel):
    name = CharField()
    instructions = TextField()
    counts = TextField()
    created = DateTimeField(default=datetime.datetime.now)