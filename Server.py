import socket
import threading

# Function to handle client connections
def handle_client(client_socket, client_address):
    print(f"Connected with {client_address}")

    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode()
        if not data:
            break
        
        print(f"Client ({client_address}): {data}")

        # Send data back to the client
        response = input("Server: ")
        client_socket.send(response.encode())

    print(f"Connection with {client_address} closed.")
    client_socket.close()

# Server configuration
HOST = 'localhost'
PORT = 8080

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(5)
print(f"Server listening on {HOST}:{PORT}")

while True:
    # Accept incoming connections
    client_socket, client_address = server_socket.accept()

    # Start a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
