from flask import Flask

app = Flask(__name__)

from routes import *


if __name__ == "__main__":
    app.secret_key = 'your_secret_key_here'

    app.run(debug=True)