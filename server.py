# server.py
import socket
import threading
import logging

# Setting up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def handle_client(client_socket):
    with client_socket:
        logging.info(f"{client_socket.getpeername()} connected")
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                client_socket.sendall(data)
                logging.info(f"Data exchanged with {client_socket.getpeername()}")
        finally:
            logging.info(f"{client_socket.getpeername()} disconnected")

def accept_connections(server_socket):
    try:
        while True:
            client_socket, addr = server_socket.accept()
            logging.info(f"Connected to {addr}")
            thread = threading.Thread(target=handle_client, args=(client_socket,))
            thread.start()
    except KeyboardInterrupt:
        logging.info("Server is shutting down.")
    finally:
        server_socket.close()

def start_server(host='localhost', port=12345):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    logging.info(f"Server is listening on {host}:{port}")
    accept_connections(server_socket)

if __name__ == "__main__":
    start_server()

