import socket
import threading

# Server setup
host = "0.0.0.0"  # Accept connections from any IP
port = 12345       # Choose a free port

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
print(f"Server running on {host}:{port}")

clients = []

# Broadcast messages to all connected clients
def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            clients.remove(client)

# Handle each client
def handle_client(client):
    while True:
        try:
            msg = client.recv(1024)
            if msg:
                broadcast(msg)
        except:
            clients.remove(client)
            break

# Accept clients
while True:
    client, addr = server.accept()
    print(f"Connected: {addr}")
    clients.append(client)
    threading.Thread(target=handle_client, args=(client,), daemon=True).start()
