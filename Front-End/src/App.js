import logo from './logo.svg';
import './App.css';
import { useState } from 'react';
function App() {

  const [movies, setMovies] = useState([]);

  async function fetchMoviesHandler () {
    const response = await fetch('http://localhost:5000/', {
      method: 'GET',
      body: {"nombre":"The man in the arena (Tom Brady story)"},
      headers: {
        'Conten-Type':'application/json'
      }
    });

    const data = await response.json();
    const loadedMovies = [];
    for (const movie in data) {
      loadedMovies.push({
        genero: data[movie].genero
      });
    }
    setMovies(loadedMovies);
  }

  return (
    <React.Fragment>
      <section>
        <button onClick={fetchMoviesHandler}>Fetch Movies</button>
      </section>
      <section>
        <MovieList movies={movies}
      </section>
    </React.Fragment>
  );
}

export default App;
