import socket

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a host and port
host = "127.0.0.1"  # Localhost
port = 8080 # Arbitrary port number
server_socket.bind((host, port))

# Listen for connections
server_socket.listen(1)
print("Server is waiting for a connection...")

# Accept connection from client
client_socket, addr = server_socket.accept()
print(f"Connected to {addr}")

# Chat loop
while True:
    # Receive message from client
    client_msg = client_socket.recv(1024).decode()
    if client_msg.lower() == 'exit':
        print("Client has exited the chat.")
        break
    print(f"Client: {client_msg}")
    
    # Send message to client
    server_msg = input("Server: ")
    client_socket.send(server_msg.encode())
    if server_msg.lower() == 'exit':
        print("Exiting the chat...")
        break

# Close the sockets
client_socket.close()
server_socket.close()