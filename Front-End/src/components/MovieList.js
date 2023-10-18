import React from "react";

import Movie from "./Movie";

function MovieList (props) {
    return (
        <ul>
            {props.movies.map((movie) => {
                <Movie 
                    genero={movie.genero}
                />
            })}
        </ul>
    );
};

export default MovieList;