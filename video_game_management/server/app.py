# app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config  # Import Config here

app = Flask(__name__)
app.config.from_object(Config)  # Now Config is defined
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import your models after initializing db to avoid circular imports
from .models import Game, Developer, Platform  # Replace with your actual models


# Create Models
class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)

    games = db.relationship('VideoGame', backref='genre', lazy=True)

    def __init__(self, name):
        self.name = name

class Platform(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)

    games = db.relationship('VideoGamePlatform', backref='platform', lazy=True)

    def __init__(self, name):
        self.name = name

class VideoGame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    release_date = db.Column(db.Date)
    price = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))

    reviews = db.relationship('Review', backref='game', lazy=True)
    platforms = db.relationship('VideoGamePlatform', backref='game', lazy=True)

    def __init__(self, name, release_date, price, genre_id):
        self.name = name
        self.release_date = release_date
        self.price = price
        self.genre_id = genre_id

class VideoGamePlatform(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)
    game_id = db.Column(db.Integer, db.ForeignKey('video_game.id'))
    platform_id = db.Column(db.Integer, db.ForeignKey('platform.id'))

    def __init__(self, price, game_id, platform_id):
        self.price = price
        self.game_id = game_id
        self.platform_id = platform_id

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String(500))
    rating = db.Column(db.Integer)
    game_id = db.Column(db.Integer, db.ForeignKey('video_game.id'))

    def __init__(self, review, rating, game_id):
        self.review = review
        self.rating = rating
        self.game_id = game_id

# Create Schemas
class GenreSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Genre

class PlatformSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Platform

class VideoGameSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = VideoGame

class VideoGamePlatformSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = VideoGamePlatform

class ReviewSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Review

# Create API Endpoints
@app.route('/api/games', methods=['POST'])
def add_game():
    data = request.json
    game = VideoGame(name=data['name'], release_date=data['release_date'], price=data['price'], genre_id=data['genre_id'])
    db.session.add(game)
    db.session.commit()
    return jsonify({"message": "Game added"}), 201

@app.route('/api/games', methods=['GET'])
def get_all_games():
    games = VideoGame.query.all()
    game_schema = VideoGameSchema(many=True)
    return jsonify(game_schema.dump(games))

@app.route('/api/games/<int:id>', methods=['GET'])
def get_game(id):
    game = VideoGame.query.get(id)
    game_schema = VideoGameSchema()
    return jsonify(game_schema.dump(game))

# Add more CRUD routes for Genre, Platform, Review, etc.

if __name__ == '__main__':
    app.run(debug=True)
