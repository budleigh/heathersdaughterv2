import logging
from flask import request
from hd import app
from src.server.db import database, Order


@app.route('/order/', methods=['POST'])
def order():
    database.connect()
    if request.method == 'POST':
        print(request)
    logging.info(request)
    database.close()
    return 'good'