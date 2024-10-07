import socket

def start_server(host='localhost', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Server is listening on {host}:{port}")
    return server_socket

def accept_connections(server_socket):
    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Connected to {addr}")
            handle_client(client_socket)
    except KeyboardInterrupt:
        print("Server is shutting down.")
    finally:
        server_socket.close()

def handle_client(client_socket):
    with client_socket:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            client_socket.sendall(data)
            print(f"Received and sent back: {data.decode()}")
