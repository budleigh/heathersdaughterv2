from flask import request
from hd import app


@app.route('/order/', methods=['POST'])
def order():
    if request.method == 'POST':
        print(request)
    return 'good'