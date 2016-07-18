import datetime
from peewee import *

database = PostgresqlDatabase(
    'hdtest', 
    user='yoozer', 
    password='Generalkdrama1{}'
)


class BaseModel(Model):

    class Meta:
        database = database


class Order(BaseModel):
    name = CharField()
    instructions = TextField()
    counts = TextField()
    created = DateTimeField(default=datetime.datetime.now)