
# Tic-Tac-Toe Game Example

This is a simple Tic-Tac-Toe game implemented using Python and sockets, designed to demonstrate a basic client-server architecture.

## How to Play:

### Start the Server
1. **Run the server.py script**: This script initializes a server that listens for incoming client connections on a specified port and handles multiple client connections simultaneously.
    ```bash
    python server.py
    ```

### Connect Clients
2. **Run the client.py script** on two different machines or terminals. This script connects to the server and allows players to send and receive game moves.
    ```bash
    python client.py
    ```

### Play the Game
3. **Players take turns entering their moves**. The first player to get three in a row wins!

## Setup and Installation

1. **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd path-to-repository
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv myenv
    source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the server and client applications as described above**.

## Technologies Used:

- **Python**: Main programming language.
- **Sockets**: Used for handling real-time communication between the server and clients.

## Additional Resources:

- [Link to Python documentation](https://docs.python.org/3/)
- [Link to sockets tutorial](https://realpython.com/python-sockets/)

## File Descriptions:

- **server.py**: Handles incoming connections, manages multiple client communications simultaneously, and logs connection events.
- **client.py**: Manages client-side connections, handles sending and receiving of game moves, and logs connection events.

## Testing and Debugging:

- **Test the server's ability to handle multiple connections** by connecting multiple clients and ensuring stable communication.
- **Verify that clients can connect and interact correctly with the server**, exchanging game moves without errors.

## Troubleshooting:

- If you encounter connection issues, ensure the server is running before starting clients.
- For any errors related to socket connections, check firewall settings and ensure no port conflicts on your network.
