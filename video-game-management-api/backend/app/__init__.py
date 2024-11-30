from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///games.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    CORS(app)

    db.init_app(app)

    with app.app_context():
        from .routes import main_bp
        app.register_blueprint(main_bp, url_prefix='/api')
        db.create_all()

    return app
