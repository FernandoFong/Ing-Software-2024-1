from alchemyClasses.Usuario import Usuario

def get_all_users():
    return Usuario.query.all()

def get_user_by_id(id):
    return Usuario.query.filter(Usuario.idUsuario == id).all()

def get_user_by_name(name):
    return Usuario.query.filter(Usuario.nombre == name).all()

def get_user_by_email(email):
    return Usuario.query.filter(Usuario.email == email).all()