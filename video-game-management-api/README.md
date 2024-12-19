# Video Game Management API

## Table of Contents
- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Frontend Setup](#frontend-setup)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Project Description

This project is a RESTful API for managing video games. It allows users to interact with a database of games, developers, and platforms through a Flask backend. The API provides endpoints for creating, reading, updating, and deleting game entries.

## Installation

To set up the project locally:

1. Clone this repository:

2. Navigate into the project directory:

3. Install Python dependencies:

4. Initialize the database:

5. Run the Flask application:

## Usage

The API provides several endpoints:

### GET /api/games
- Retrieves all games from the database

### POST /api/games
- Creates a new game entry
  - Request body should include `title`, `release_date`, and `developer_id`
  - Returns the newly created game with its ID

### GET /api/games/:id
- Retrieves a specific game by its ID

### PUT /api/games/:id
- Updates an existing game
  - Request body should include fields to update (e.g., `title`, `release_date`)

### DELETE /api/games/:id
- Deletes a game by its ID

## API Documentation

For detailed API documentation, please refer to the [API Specification](./backend/API.md) file in the project root.

## Frontend Setup

This project includes a React frontend that interacts with the API. To set it up:

1. Navigate to the frontend directory:

2. Install npm dependencies:

3. Start the React development server:

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](./LICENSE.md) file for details.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [React](https://reactjs.org/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/)
