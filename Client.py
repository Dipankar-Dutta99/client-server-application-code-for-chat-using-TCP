import socket

# Client configuration
HOST = 'localhost'
PORT = 8080

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

while True:
    # Send message to the server
    message = input("Client: ")
    client_socket.send(message.encode())

    # Receive response from the server
    response = client_socket.recv(1024).decode()
    print(f"Server: {response}")

# Close the connection
client_socket.close()
