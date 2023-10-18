from alchemyClasses import db
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Boolean
from datetime import date

from model.model_pelicula import get_movie_by_id
from model.model_usuario import get_user_by_id

class Renta(db.Model):

    __tablename__ = 'rentar'
    idRentar = Column(Integer, primary_key=True)
    idUsuario = Column(Integer, ForeignKey('usuarios.idUsuario'))
    idPelicula = Column(Integer, ForeignKey('peliculas.idPelicula'))
    fecha_renta = Column(DateTime)
    dias_de_renta = Column(Integer)
    estatus = Column(Boolean)

    def __init__(self, idUsuario, idPelicula, fechaRenta=date.today()):
        self.idUsuario = idUsuario
        self.idPelicula = idPelicula
        self.fechaRenta = fechaRenta

    def __str__(self):
        usuario = get_user_by_id(self.idUsuario)
        peli = get_movie_by_id(self.idPelicula)
        return f'Renta: {self.idRenta}\nUsuario: {usuario.nombre}\nPelicula: {peli.nombre}'