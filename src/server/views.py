from flask import render_template
from hd import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/order/')
def order():
    return render_template('order.html')