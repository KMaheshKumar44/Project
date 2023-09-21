import socket
import json

# Define the host and port on which the listener service should listen
listener_host = 'localhost'
listener_port = 12345

# Create a socket to listen for incoming connections
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((listener_host, listener_port))
server_socket.listen(1)  # Listen for one incoming connection

print(f"Listening on {listener_host}:{listener_port}")

# Accept an incoming connection
client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")

while True:
    # Receive the JSON message from the emitter service
    json_message = client_socket.recv(1024).decode()

    # Parse the JSON message
    message_stream = json.loads(json_message)

    print(f"Received: {message_stream}")

# Close the sockets (this will not be reached in this example)
client_socket.close()
server_socket.close()
