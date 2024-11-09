import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import GameList from './GameList';
import GameDetail from './GameDetail';
import AddGameForm from './AddGameForm';

function App() {
    return (
        <Router>
            <Switch>
                <Route exact path="/" component={GameList} />
                <Route path="/games/:id" component={GameDetail} />
                <Route path="/add-game" component={AddGameForm} />
            </Switch>
        </Router>
    );
}

export default App;
