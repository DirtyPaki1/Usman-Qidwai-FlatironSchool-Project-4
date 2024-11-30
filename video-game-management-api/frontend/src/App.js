// App.js
import { BrowserRouter as Router, Route, Switch, Link } from 'react-router-dom';
import { useState } from 'react';
import GameList from './GameList';
import AddGame from './AddGame';
import EditGame from './EditGame';
import './index.css';

function App() {
  // State to manage the list of games
  const [games, setGames] = useState([]);

  // Function to handle adding a game
  const handleGameAdded = (newGame) => {
    setGames((prevGames) => [...prevGames, newGame]);
  };

  // Function to handle updating a game
  const handleGameUpdated = (updatedGame) => {
    setGames((prevGames) =>
      prevGames.map((game) =>
        game.id === updatedGame.id ? updatedGame : game
      )
    );
  };

  return (
    <Router>
      <div>
        <h1>Video Game Management System</h1>
        <nav>
          <ul>
            <li><Link to="/">Game List</Link></li>
            <li><Link to="/add-game">Add Game</Link></li>
          </ul>
        </nav>
        <Switch>
          {/* Pass the games list and state handler to GameList */}
          <Route exact path="/">
            <GameList games={games} />
          </Route>

          {/* Pass the onGameAdded prop to AddGame */}
          <Route path="/add-game">
            <AddGame onGameAdded={handleGameAdded} />
          </Route>

          {/* Pass the onGameUpdated prop to EditGame */}
          <Route path="/edit-game/:id">
            <EditGame onGameUpdated={handleGameUpdated} />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

export default App;
