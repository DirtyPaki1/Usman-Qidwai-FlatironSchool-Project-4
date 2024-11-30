from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Sample data for games
games = [
    {"id": 1, "title": "Game 1", "release_date": "2023-01-01"},
    {"id": 2, "title": "Game 2", "release_date": "2022-01-01"}
]

@app.route('/')
def home():
    # Added a home route to handle 404 errors when hitting the base URL.
    return jsonify({"message": "Welcome to the Game API!"})

@app.route('/api/games', methods=['GET', 'POST'])
def handle_games():
    if request.method == 'GET':
        try:
            # Return the list of games as JSON response
            return jsonify(games), 200
        except Exception as e:
            app.logger.error(f"Error fetching games: {str(e)}")
            return jsonify({"error": "Internal server error", "message": str(e)}), 500

    if request.method == 'POST':
        try:
            # Get the data sent in the POST request
            game_data = request.get_json()

            # Validation: check if required fields are present
            if not game_data or not all(key in game_data for key in ['title', 'release_date']):
                return jsonify({"error": "Missing required fields: 'title' and 'release_date'"}), 400

            # Generate a new ID (ensure it's unique)
            new_id = max((game['id'] for game in games), default=0) + 1

            # Create a new game entry
            new_game = {
                "id": new_id,
                "title": game_data['title'],
                "release_date": game_data['release_date']
            }
            games.append(new_game)

            # Return the newly created game
            return jsonify(new_game), 201
        except Exception as e:
            app.logger.error(f"Error adding game: {str(e)}")
            return jsonify({"error": "Internal server error", "message": str(e)}), 500

@app.route('/api/games/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_game(id):
    # Find the game with the given ID
    game = next((game for game in games if game['id'] == id), None)

    if request.method == 'GET':
        if game:
            return jsonify(game), 200
        return jsonify({'error': 'Game not found'}), 404

    if request.method == 'PUT':
        if not game:
            return jsonify({'error': 'Game not found'}), 404
        
        try:
            # Get the data to update the game
            game_data = request.get_json()

            # Validation for empty update payload
            if not game_data:
                return jsonify({"error": "No data provided for update"}), 400

            # Update the game's attributes
            game['title'] = game_data.get('title', game['title'])
            game['release_date'] = game_data.get('release_date', game['release_date'])

            return jsonify(game), 200
        except Exception as e:
            app.logger.error(f"Error updating game: {str(e)}")
            return jsonify({"error": "Internal server error", "message": str(e)}), 500

    if request.method == 'DELETE':
        if not game:
            return jsonify({'error': 'Game not found'}), 404
        
        try:
            # Remove the game from the list
            games.remove(game)
            return jsonify({'message': 'Game deleted successfully'}), 200
        except Exception as e:
            app.logger.error(f"Error deleting game: {str(e)}")
            return jsonify({"error": "Internal server error", "message": str(e)}), 500

if __name__ == '__main__':
    # Run the app in debug mode to see detailed error messages
    app.run(debug=True)
