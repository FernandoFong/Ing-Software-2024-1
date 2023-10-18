from alchemyClasses.Pelicula import Pelicula

def get_all_movies():
    return Pelicula.query.all()

def get_movie_by_id(id):
    return Pelicula.query.filter(Pelicula.idPelicula == id)

def get_movie_by_name(name):
    return Pelicula.query.filter(Pelicula.nombre == name)