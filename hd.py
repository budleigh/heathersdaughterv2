from flask import Flask
app = Flask(__name__)

import src.server.views
import src.server.api

if __name__ == '__main__':
    app.run()
