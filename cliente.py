import socket

# Configuración del cliente
host = '192.168.1.5'  # Dirección IP del servidor
port = 5000  # Puerto para la conexión

# Crear un socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar al servidor
client_socket.connect((host, port))

# Enviar el nombre del estudiante
student_name = input('Ingrese su nombre: ')
client_socket.send(student_name.encode('utf-8'))

# Esperar por la respuesta del servidor antes de enviar más mensajes
response = client_socket.recv(1024).decode('utf-8')
print(response)

# Enviar mensajes hasta que se ingrese la palabra "desconectar"
while True:
    message = input('Ingrese un mensaje: ')
    client_socket.send(message.encode('utf-8'))
    if message == 'desconectar':
        break

# Cerrar la conexión con el servidor
client_socket.close()
print('Conexión cerrada con el servidor')




