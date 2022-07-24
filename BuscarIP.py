# socket - Este módulo proporciona operaciones de socket y algunas funciones relacionadas.
import socket

# gethostname - Sirve para conseguir el nombre del sistema o equipo en donde se ejecuta.
name = socket.gethostname()

# gesthostbyname - Sirve para conseguir la direccion ip del host.
ip = socket.gethostbyname(name)

print(f'El nombre de tu PC es: {name}')
print(f'Tu direccion IP es: {ip}')