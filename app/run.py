from app.adaptor import file_routes as file
from app.domain.model import Usuario

print('Iniciando')
usuario = Usuario('Jorgear77', 'Jorge', 'Rodriguez')
file.create_file("archprueba.txt", usuario)