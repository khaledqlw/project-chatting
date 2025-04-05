import socket

try:
    
    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   
    # Connect to server
    host = "127.0.0.1"  # Match the server's host
    port = 8080 # Match the server's port
    client_socket.connect((host, port))
    print("Connected to the server!")

    # Chat loop
    while True:
        # Send message to server
        client_msg = input("Client: ")
        client_socket.send(client_msg.encode())
        if client_msg.lower() == 'exit':
            print("Exiting the chat...")
            break

        # Receive message from server
        server_msg = client_socket.recv(1024).decode()
        print(f"Server: {server_msg}")
        if server_msg.lower() == 'exit':
            print("Server has exited the chat.")
            break

    # Close the socket
    client_socket.close()

except ConnectionRefusedError:
    print("Could not connect to the server. Make sure the server is running.")
except Exception as e:
    print(f"An error occurred: {e}")