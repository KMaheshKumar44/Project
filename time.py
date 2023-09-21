import socket
import time
import json

# Define the target host and port where the listener service is running
listener_host = 'localhost'
listener_port = 12345  # Replace with the actual port of the listener service

# Create a socket to connect to the listener service
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((listener_host, listener_port))

while True:
    # Create a new message stream (you can modify this as needed)
    message_stream = {
        'data': 'This is a new message stream.',
        'timestamp': time.time()
    }

    # Convert the message stream to a JSON string
    json_message = json.dumps(message_stream)

    # Send the JSON message to the listener service
    client_socket.send(json_message.encode())

    print(f"Sent: {json_message}")

    # Wait for 10 seconds before sending the next message
    time.sleep(10)

# Close the socket (this will not be reached in this example)
client_socket.close()
