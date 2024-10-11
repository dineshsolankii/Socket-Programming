import socket

# Define server address and port
SERVER_HOST = 'big-women-build.loca.lt'  # Replace with your Localtunnel URL
SERVER_PORT = 80  # Localtunnel uses port 80

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    print("Connected to server")

    # Send data to server
    while True:
        message = input("Enter your name (type 'exit' to quit): ")
        if message.lower() == 'exit':
            break
        client_socket.sendall(message.encode('utf-8')) # Encoding

        # Receive data from server
        data = client_socket.recv(1024)
        print(f"Received from server: {data.decode('utf-8')}")
finally:
    # Close the socket
    client_socket.close()
    print("Connection closed.")
