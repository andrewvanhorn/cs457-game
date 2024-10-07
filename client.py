# client.py
import socket
import logging

# Setting up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def connect_to_server(host='localhost', port=12345):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        logging.info(f"Connected to server at {host}:{port}")
        return client_socket
    except socket.error as e:
        logging.error(f"Failed to connect to {host}:{port}, error: {e}")
        return None

def send_and_receive_messages(client_socket):
    if client_socket is None:
        return
    try:
        while True:
            message = input("Enter message: ")
            if message.lower() == 'exit':
                break
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024)
            print(f"Received from server: {data.decode()}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        client_socket.close()
        logging.info("Disconnected from server")

if __name__ == "__main__":
    client_socket = connect_to_server()
    send_and_receive_messages(client_socket)
