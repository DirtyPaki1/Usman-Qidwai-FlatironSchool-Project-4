from flask import Blueprint, request, jsonify
from .models import Game, Developer
from . import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/games', methods=['POST'])
def add_game():
    try:
        data = request.get_json()

        # Ensure all required fields are provided
        if not all(k in data for k in ('title', 'release_date', 'developer_id')):
            return jsonify({'error': 'Missing required fields'}), 400

        # Validate developer_id
        developer = Developer.query.get(data['developer_id'])
        if not developer:
            return jsonify({'error': 'Developer not found'}), 400

        # Create the new game instance with all required fields
        new_game = Game(
            title=data['title'],
            release_date=data['release_date'],
            developer_id=data['developer_id']  # Ensure developer_id is included
        )

        # Add the game to the database
        db.session.add(new_game)
        db.session.commit()

        # Return the new game as a JSON response
        return jsonify({
            'game': {
                'id': new_game.id,
                'title': new_game.title,
                'release_date': new_game.release_date,
                'developer': developer.name
            }
        }), 201
    
    except Exception as e:
        # Log the error for debugging and rollback the session
        db.session.rollback()  # Ensure the session is properly rolled back on error
        print(f"Error occurred while adding game: {e}")
        return jsonify({'error': 'Internal server error', 'details': str(e)}), 500
