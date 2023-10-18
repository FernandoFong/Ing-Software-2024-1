from alchemyClasses import db
from sqlalchemy import Column, Integer, String
from hashlib import sha256
from CryptoUtils.CryptoUtils import cipher

class Usuario(db.Model):

    __tablename__ = 'usuarios'
    idUsuario = Column(Integer, primary_key=True)
    nombre = Column(String(200))
    email = Column(String(500), unique=True)
    password = Column(String(64))

    def __init__(self, nombre, email, passwd):
        self.nombre = nombre
        self.email = email
        self.password = sha256(cipher(passwd)).hexdigest()

    def __str__(self):
        return f'idUsuario: {self.idUsuario}\nnombre: {self.nombre}\ncorreo: {self.email}'