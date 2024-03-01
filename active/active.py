import argparse
import socket

def scan_udp_port(ip, port, timeout=1):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.settimeout(timeout)
            # Sending a test packet
            s.sendto(b'test', (ip, port))
            try:
                # Waiting for a response
                data, _ = s.recvfrom(4096)
                print(f"Received data from port {port}: {data}")
                print(f"Port {port} (UDP) is open.")
                return port, True  # Data received, port is open
            except socket.timeout:
                print(f"Port {port} (UDP) is closed (timeout).")
                return port, False  # No response, port is closed.
            except socket.error as e:
                print(f"Error on port {port}: {e}")
                return port, False  # An error occurred, port is closed.
    except socket.gaierror as e:
        print(f"Address-related error: {e}")
        return port, False  # Error related to the address.
    except socket.error as e:
        print(f"Error creating socket: {e}")
        return port, False  # Error while creating the socket



def scan_tcp_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((ip, port))
            if result == 0:
                return port, True
            else:
                return port, False
    except socket.error as e:
        print(f"Error on port {port}: {e}")
        return port, False


def parse_port_range(port_range):
    if "-" in port_range:
        start_port, end_port = map(int, port_range.split("-"))
        return range(start_port, end_port + 1)
    else:
        return [int(port_range)]

def scan_ports(ip, ports, is_tcp=True):
    for port in ports:
        if is_tcp:
            _, is_open = scan_tcp_port(ip, port)
            protocol = "TCP"
        else:
            _, is_open = scan_udp_port(ip, port)
            protocol = "UDP"

        status = "open" if is_open else "closed"
        print(f"Port {port} ({protocol}) is {status}.")


def main():    
    parser = argparse.ArgumentParser(description="TinyScanner - Simple Port Scanner")
    parser.add_argument("host", type=str, help="Host to scan")
    parser.add_argument("-p", "--ports", type=str, help="Range of ports to scan")
    parser.add_argument("-u", "--udp", action="store_true", help="UDP scan")
    parser.add_argument("-t", "--tcp", action="store_true", help="TCP scan")

    args = parser.parse_args()
    ports = parse_port_range(args.ports)
    if args.udp:
        scan_ports(args.host, ports, is_tcp=False)
    else:
        scan_ports(args.host, ports)

if __name__ == "__main__":
    main()
