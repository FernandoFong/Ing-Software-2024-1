from alchemyClasses import db
from sqlalchemy import Column, Integer, String

class Pelicula(db.Model):

    __tablename__ = 'peliculas'
    idPelicula = Column(Integer, primary_key=True)
    nombre = Column(String(200))
    genero = Column(String(45))
    duracion = Column(Integer)
    inventario = Column(Integer)

    def __init__(self, nombre, genero, duracion=120, invent=5):
        self.nombre=nombre
        self.genero=genero
        self.duracion=duracion
        self.inventario=invent

    def __str__(self):
        return f'f{self.nombre}'