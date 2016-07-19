from flask import Flask
app = Flask(__name__)

from src.server.views import *
from src.server.api import *

if __name__ == '__main__':
    app.run()
