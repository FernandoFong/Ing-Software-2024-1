from flask import Blueprint, session, g, request
import json

from model.model_pelicula import get_movie_by_id, get_all_movies, get_movie_by_name
from model.model_renta import rents_by_email
from model.model_usuario import get_all_users, get_user_by_id

json_controller = Blueprint('json', __name__, url_prefix='/json')

@json_controller.route('/users')
def get_users():
    users = get_all_users()
    response = []
    for user in users:
        response.append({
            'nombre':user.nombre,
            'correo':user.email
        })
    return json.dumps(response)

@json_controller.route('/rents_by_session')
def get_rents_by_user():
    if session.get('user', None) is None:
        return json.dumps({
            'error': 'Cookie de sesion vacia'
        })
    email = session.get('email')
    rentas = rents_by_email(email)
    response = []
    for renta in rentas:
        response.append({
            'idUsuario': get_user_by_id(renta.idUsuario)[0].nombre,
            'idPelicula': get_movie_by_id(renta.idPelicula)[0].nombre
        })
    return json.dumps(response)

@json_controller.route('/movie_json')
def get_movie():
    nombre = request.json.get("nombre", None)
    if nombre is None:
        return {'error':'Nombre is required'}
    movie = get_movie_by_name(nombre)
    if movie is []:
        return {'error':'Movie not found'}
    return json.dumps({
        'genero':movie[0].genero
    })