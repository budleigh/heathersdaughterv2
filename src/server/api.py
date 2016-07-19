import logging
from flask import request
from hd import app


@app.route('/order/', methods=['POST'])
def order():
    return 'good'