import React, { useState, useEffect } from 'react';
import { useParams, useHistory } from 'react-router-dom';

const EditGame = ({ onGameUpdated }) => {
  const { id } = useParams();  // Extract game ID from the URL
  const history = useHistory();  // For navigation after update

  const [game, setGame] = useState({
    title: '',
    release_date: '',
  });

  useEffect(() => {
    // Fetch the game details from the backend
    fetch(`http://127.0.0.1:5000/api/games/${id}`)
      .then((response) => response.json())
      .then((data) => {
        if (data.error) {
          console.error('Game not found:', data.error);
          return;
        }
        setGame({ title: data.title, release_date: data.release_date });
      })
      .catch((error) => console.error('Error fetching game:', error));
  }, [id]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setGame({ ...game, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch(`http://127.0.0.1:5000/api/games/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(game),
      });

      if (!response.ok) {
        throw new Error('Failed to update game');
      }

      const updatedGame = await response.json();
      onGameUpdated(updatedGame);  // Notify parent about the update
      history.push('/');  // Navigate back to the game list
    } catch (error) {
      console.error('Error updating game:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Title:</label>
        <input
          type="text"
          name="title"
          value={game.title}
          onChange={handleChange}
        />
      </div>
      <div>
        <label>Release Date:</label>
        <input
          type="date"
          name="release_date"
          value={game.release_date}
          onChange={handleChange}
        />
      </div>
      <button type="submit">Update Game</button>
    </form>
  );
};

export default EditGame;
