# Empty
"""Methods for altering the file tables"""
from app.infrastructure import file_repository


def get_file(nombre):
    """Get a file"""
    return file_repository.get_file(nombre)


def post_file(nombre, contenido):
    """Create an new file"""
    if len(contenido[1]) < 6:
        nombre = contenido[1]
    else:
        nombre = contenido[2] + ' ' + contenido[3]   

    if not nombre.istitle():
        print("Usuario es invalido")
    else:
        file_repository.post_file(nombre, contenido)
