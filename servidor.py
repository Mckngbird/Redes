import socket

# Configuración del servidor
host = '192.168.1.5'  # Dirección IP del servidor
port = '5000'  # Puerto para la conexión
max_connections = 5  # Número máximo de conexiones encoladas

# Crear un socket TCP/IP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincular el socket al host y puerto
server_socket.bind((host, port))

# Escuchar conexiones entrantes
server_socket.listen(5)

print('El servidor está listo para recibir conexiones...')

connected_clients = []  # Lista para almacenar los nombres de los clientes conectados

while True:
    # Aceptar una conexión entrante
    client_socket, client_address = server_socket.accept()
    print(f'Cliente conectado desde: {client_address}')

    # Verificar si hay demasiadas conexiones activas
    if len(connected_clients) >= max_connections:
        message = 'El servidor está ocupado. Por favor, espera.'
        client_socket.send(message.encode('utf-8'))
        client_socket.close()
        continue

    # Solicitar el nombre del estudiante
    client_socket.send(b'Gracias por conectarse al servidor')
    student_name = client_socket.recv(1024).decode('utf-8')
    connected_clients.append((client_socket, student_name))

    print(f'Nombre del estudiante: {student_name}')

    # Recibir mensajes del cliente hasta que se reciba la palabra "desconectar"
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        print(f'Mensaje recibido de {student_name}: {data}')
        if data == 'desconectar':
            break

    # Eliminar al cliente de la lista de conexiones
    connected_clients.remove((client_socket, student_name))

    # Cerrar la conexión con el cliente
    client_socket.close()
    print('Conexión cerrada con el cliente')



