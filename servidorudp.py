import socket

# Configuración del servidor
host = '192.168.1.5'  # Dirección IP del servidor
port = 5000  # Puerto para la conexión
max_connections = 5 

# Crear un socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Vincular el socket al host y puerto
server_socket.bind((host, port))

print('El servidor está listo para recibir conexiones...')

connected_clients = {}  # Diccionario para almacenar los nombres de los clientes conectados

while True:
    # Recibir datos y dirección del cliente
    data, client_address = server_socket.recvfrom(1024)
    print(f'Cliente conectado desde: {client_address}')

    # Verificar si hay demasiadas conexiones activas
    if len(connected_clients) >= max_connections:
        message = 'El servidor está ocupado. Por favor, espera.'
        server_socket.sendto(message.encode('utf-8'), client_address)
        continue

    # Solicitar el nombre del estudiante
    server_socket.sendto(b'Gracias por conectarse al servidor', client_address)
    student_name = data.decode('utf-8')
    connected_clients[client_address] = student_name

    print(f'Nombre del estudiante: {student_name}')

    # Recibir mensajes del cliente hasta que se reciba la palabra "desconectar"
    while True:
        data, _ = server_socket.recvfrom(1024)
        print(f'Mensaje recibido de {student_name}: {data.decode("utf-8")}')
        if data.decode('utf-8') == 'desconectar':
            break

    # Eliminar al cliente de la lista de conexiones
    connected_clients.pop(client_address)

    print('Conexión cerrada con el cliente')
