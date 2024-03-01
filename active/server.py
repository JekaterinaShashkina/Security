import socket

def udp_server(port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        server_address = ('', port)
        s.bind(server_address)
        print(f"UDP server listening on port {port}")

        while True:
            data, address = s.recvfrom(4096)
            print(f"Received data from {address}: {data}")
            if data:
                s.sendto(b'ack', address)

udp_server(8080)
