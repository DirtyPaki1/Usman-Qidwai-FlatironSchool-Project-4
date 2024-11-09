# Usman-Qidwai-FlatironSchool-Project-4

Video Game Management API

This project is a RESTful API for managing information about video games, genres, platforms, and reviews. Built with Flask and SQLAlchemy, the API allows CRUD operations for games, genres, platforms, and reviews, enabling users to create, retrieve, update, and delete data with ease.

Features

Manage information about video games, including name, release date, price, genre, platforms, and reviews.
CRUD functionality for each entity (VideoGame, Genre, Platform, Review).
JSON responses for easy integration with frontend applications.
Data validation and schema serialization with Flask-Marshmallow and Marshmallow-SQLAlchemy.
Requirements

To install and run this project, you need:

Python 3.7 or higher
Pipenv for virtual environment management
Flask and related libraries (Flask-SQLAlchemy, Flask-Marshmallow, Marshmallow-SQLAlchemy)
Setup

Clone the repository:
git clone https://github.com/yourusername/video_game_management_api.git
cd video_game_management_api
Set up the virtual environment and install dependencies:
pipenv install
Activate the virtual environment:
pipenv shell
Set up the database:
Configure the database URI in app.py under app.config['SQLALCHEMY_DATABASE_URI'].
By default, this README assumes you are using SQLite, but you may modify the URI for other databases.
Initialize the database:
flask db init
flask db migrate
flask db upgrade
Run the application:
flask run
The server will start on http://127.0.0.1:5000.
Endpoints

Games
Create a new game
POST /api/games
Payload: { "name": "Game Name", "release_date": "YYYY-MM-DD", "price": 59.99, "genre_id": 1 }
Retrieve all games
GET /api/games
Retrieve a specific game
GET /api/games/<int:id>
Genres
Create a new genre
POST /api/genres
Payload: { "name": "Genre Name" }
Retrieve all genres
GET /api/genres
Retrieve a specific genre
GET /api/genres/<int:id>
Platforms
Create a new platform
POST /api/platforms
Payload: { "name": "Platform Name" }
Retrieve all platforms
GET /api/platforms
Retrieve a specific platform
GET /api/platforms/<int:id>
Reviews
Create a new review
POST /api/reviews
Payload: { "review": "Great game!", "rating": 5, "game_id": 1 }
Retrieve all reviews
GET /api/reviews
Retrieve a specific review
GET /api/reviews/<int:id>
Technologies Used

Backend: Python, Flask
Database: SQLAlchemy
Serialization: Marshmallow, Flask-Marshmallow

