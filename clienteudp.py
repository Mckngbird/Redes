import socket

# Configuración del cliente
host = '192.168.1.5'  # Dirección IP del servidor
port = 5000  # Puerto para la conexión

# Crear un socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enviar el nombre del estudiante
student_name = input('Ingrese su nombre: ')
client_socket.sendto(student_name.encode('utf-8'), (host, port))

# Esperar por la respuesta del servidor antes de enviar más mensajes
response, _ = client_socket.recvfrom(1024)
print(response.decode('utf-8'))

# Enviar mensajes hasta que se ingrese la palabra "desconectar"
while True:
    message = input('Ingrese un mensaje: ')
    client_socket.sendto(message.encode('utf-8'), (host, port))
    if message == 'desconectar':
        break

# Cerrar el socket
client_socket.close()
print('Conexión cerrada con el servidor')

