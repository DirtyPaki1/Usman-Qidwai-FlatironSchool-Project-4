import axios from 'axios';

const apiUrl = 'http://localhost:5000/api';

export const fetchGames = () => axios.get(`${apiUrl}/games`);
export const fetchGame = (id) => axios.get(`${apiUrl}/games/${id}`);
export const addGame = (gameData) => axios.post(`${apiUrl}/games`, gameData);
