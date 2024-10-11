import socket

# Define host and port
HOST = '0.0.0.0'  # Bind to all available interfaces
PORT = 1002       # Port to listen on (non-privileged ports are > 1023)

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(5)
print(f"Server is listening on {HOST}:{PORT}...")

# Accept a client connection
client_socket, client_address = server_socket.accept()
print(f"Connected to client at {client_address}")

custom_msg = ""
# Receive data from client
while True:
    data = client_socket.recv(1024)
    if not data:
        break
    else:
        decoded_data = data.decode()
        custom_msg = f"Hello Good morning !!!! ::: {decoded_data}"
        print(f"Received from client: {decoded_data}")

    # Echo back to client
    client_socket.sendall(custom_msg.encode())

# Close the sockets
client_socket.close()
server_socket.close()
print("Connection closed.")
