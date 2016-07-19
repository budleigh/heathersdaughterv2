import json
import logging
from flask import request
from hd import app
from src.server.db import *


@app.route('/order/', methods=['POST'])
def order():
    logging.error(request.get_data())
    save_order(json.loads(request.get_data().decode()))
    return 'ok'


@app.route('/orders/', methods=['GET'])
def orders():
    return json.dumps(get_orders())


@app.route('/auth/', methods=['POST'])
def auth():
    return 'ok'