from alchemyClasses.Renta import Renta
from model.model_usuario import get_user_by_email

def rents_by_email(email):
    usuario = get_user_by_email(email)
    if usuario is []:
        return []
    usuario = usuario[0]
    return Renta.query.filter(Renta.idUsuario == usuario.idUsuario).all()