import datetime
import os
from peewee import *
from playhouse.db_url import connect

db_url = os.environ.get(
    'DATABASE_URL', 
    'postgres://postgres:valerie1@localhost:5432/hdtest'
)
database = connect(db_url)


class BaseModel(Model):

    class Meta:
        database = database


class Order(BaseModel):
    name = CharField()
    instructions = TextField()
    counts = TextField()
    created = DateTimeField(default=datetime.datetime.now)