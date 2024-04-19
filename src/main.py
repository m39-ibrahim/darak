from flask import Flask
app = Flask(__name__)

from routes import *


if __name__ == "__main__":
    app.secret_key = 'your_secret_key_here'
    app.register_blueprint(category_bp)
    app.register_blueprint(section_bp)
    app.register_blueprint(favorites_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(search_bp)
    
    app.run(debug=True)