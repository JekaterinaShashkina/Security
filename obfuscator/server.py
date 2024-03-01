import socket

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 2222 

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER_HOST, SERVER_PORT))
server.listen(5)
print(f"Listening as {SERVER_HOST}:{SERVER_PORT} ...")

client_socket, client_address = server.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")

while True:
    command = input("Enter command: ")
    client_socket.send(command.encode())
    if command.lower() == 'exit':
        break
    results = client_socket.recv(4096).decode()
    print(results)

client_socket.close()
server.close()
