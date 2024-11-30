import React, { useState } from 'react';

function AddGame({ onGameAdded }) {
  const [title, setTitle] = useState('');
  const [releaseDate, setReleaseDate] = useState('');
  const [developerId, setDeveloperId] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Validation: ensure all fields are filled out
    if (!title || !releaseDate || !developerId) {
      setError('All fields are required.');
      return;
    }

    try {
      // Send a POST request to the backend to add the game
      const response = await fetch('http://127.0.0.1:5000/api/games', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          title,
          release_date: releaseDate,
          developer_id: parseInt(developerId, 10), // Ensure developerId is an integer
        }),
      });

      // If the response is not okay, throw an error
      if (!response.ok) {
        const errorData = await response.json();
        setError(errorData.error || 'Failed to add the game');
        throw new Error(errorData.error || 'Failed to add the game');
      }

      // Parse the JSON response
      const newGame = await response.json();

      // Call the onGameAdded callback with the new game data
      onGameAdded(newGame.game);

      // Clear the form fields
      setTitle('');
      setReleaseDate('');
      setDeveloperId('');
      setError('');
    } catch (error) {
      // Log and display the error
      console.error('Error adding game:', error);
      setError(error.message || 'Failed to add game. Please try again.');
    }
  };

  return (
    <div>
      <h2>Add a New Game</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <form onSubmit={handleSubmit}>
        <div>
          <label>Title:</label>
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
        </div>
        <div>
          <label>Release Date:</label>
          <input
            type="date"
            value={releaseDate}
            onChange={(e) => setReleaseDate(e.target.value)}
          />
        </div>
        <div>
          <label>Developer ID:</label>
          <input
            type="number"
            value={developerId}
            onChange={(e) => setDeveloperId(e.target.value)}
          />
        </div>
        <button type="submit">Add Game</button>
      </form>
    </div>
  );
}

export default AddGame;
