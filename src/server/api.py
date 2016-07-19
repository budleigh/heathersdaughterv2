import json
import logging
from flask import request
from hd import app
from src.server.db import *

valid_sessions = set()


@app.route('/order/', methods=['POST'])
def order():
    save_order(json.loads(request.get_data().decode()))
    return 'ok'


@app.route('/orders/', methods=['POST'])
def orders():
    return json.dumps([order for order in get_orders()])


@app.route('/auth/', methods=['POST'])
def auth():
    if request.form['username'] == 'xfwbird' and request.form['password'] == 'tubular':
        valid_sessions.add(request.form['sessionId'])
        return 'ok'
    else:
        raise Exception('bad admin access attempt')


@app.route('/logout/', methods=['POST'])
def logout():
    valid_sessions.remove(request.form['sessionId'])
    return 'ok'