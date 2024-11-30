import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

const GameList = () => {
  const [games, setGames] = useState([]);
  const [loading, setLoading] = useState(true); // State for loading
  const [error, setError] = useState(null);    // State for errors

  useEffect(() => {
    // Fetch games from the backend
    const fetchGames = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5000/api/games'); // Adjusted URL
        if (!response.ok) {
          throw new Error(`Failed to fetch games: ${response.statusText}`);
        }

        const data = await response.json();
        setGames(data);
        setError(null); // Clear any previous errors
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false); // Ensure loading is stopped
      }
    };

    fetchGames();
  }, []);

  const handleDelete = async (id) => {
    try {
      const response = await fetch(`http://127.0.0.1:5000/api/games/${id}`, {
        method: 'DELETE',
      });

      if (!response.ok) {
        throw new Error('Failed to delete game');
      }

      // Update the game list by filtering out the deleted game
      setGames((prevGames) => prevGames.filter((game) => game.id !== id));
    } catch (err) {
      console.error('Error deleting game:', err);
      setError('Unable to delete the game. Please try again later.');
    }
  };

  // Conditional rendering for loading, error, and games list
  if (loading) {
    return <p>Loading games...</p>;
  }

  if (error) {
    return <p>Error: {error}</p>;
  }

  return (
    <div>
      <h1>Game List</h1>
      {games.length > 0 ? (
        <ul>
          {games.map((game) => (
            <li key={game.id}>
              <h3>{game.title}</h3>
              <p>Release Date: {game.release_date}</p>
              <Link to={`/edit-game/${game.id}`}>Edit</Link>
              <button onClick={() => handleDelete(game.id)}>Delete</button>
            </li>
          ))}
        </ul>
      ) : (
        <p>No games available</p>
      )}
    </div>
  );
};

export default GameList;
