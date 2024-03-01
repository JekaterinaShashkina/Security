# Active

Active is a command-line tool for scanning TCP and UDP ports. It allows users to check if ports on a specified IP address are open and identify the services using these ports.

## Installation

Python version 3.x is required to use the port scanner. No additional dependencies are needed.

## Usage

To run a scan, use the following syntax in the command line:
**python active.py <IP-address> -p <ports> [-u] [-t]**

- <IP-address>: The IP address of the target device for scanning.
- <ports>: A single port or a range of ports to scan (e.g., 80 or 80-100).
- -u: Flag for scanning UDP ports (TCP ports are scanned by default).
- -t: Flag for scanning TCP ports.

### Important Note for UDP Scanning

Before scanning UDP ports, ensure that a UDP server is running on the target device. The scanner checks for responsiveness of the ports and requires an active UDP service to accurately determine if the ports are open.

To start the UDP server, enter the command **python server.py**. The server will run on port 8080.

## Examples

Before using, check in terminal which TCP ports are open on your system.
For this, in Windows, use the command **netstat -an | find "LISTENING"** and in Linux, use **netstat -an | grep LISTEN**.

Scanning TCP port 80
**python active.py 192.168.1.1 -p 80 -t**

Scanning UDP ports from 80 to 90
**python active.py 192.168.1.1 -p 8080-9000 -u**

## Explanation about Ports and Port scanning

A port in computer networking refers to an endpoint or a logical access point for communications in an operating system. It helps to differentiate traffic intended for different services or applications running on a single network address. Each port is identified by a number, known as the port number, which is associated with a specific process or service.
Ports are crucial in the TCP/IP networking model, where they serve to route data to the correct application on a network. There are two main types of ports:

1. TCP (Transmission Control Protocol) Ports: These are used for reliable, ordered, and error-checked delivery of data between applications. TCP ports ensure that data packets are delivered in sequence and without errors, making them suitable for applications where data integrity is crucial, such as web browsing, email, and file transfers.

2. UDP (User Datagram Protocol) Ports: These are used for simpler, connectionless communication that doesn't require the reliability of TCP. UDP ports are used in situations where speed is more critical than reliability, such as streaming media, online games, and voice or video communications.

Ports range from 0 to 65535, with the ports from 0 to 1023 known as "well-known ports" assigned to common protocols and services by the Internet Assigned Numbers Authority (IANA).

## Port scanning

Port scanning is a method used in networking to identify open ports on a networked device. This technique is often used in network security to detect vulnerable services that might be susceptible to exploitation. Here's an explanation of port scanning in more detail:

### What is Port Scanning?

**Port Scanning Basics:** Port scanning involves sending messages to each port on a device and observing the responses. By doing this, one can determine which ports are open (i.e., ready to receive data), closed (i.e., not prepared to receive data), or filtered (i.e., managed by a firewall or network filter).

**Purpose:** The primary goal is to map out the network infrastructure of a target system, including identifying open ports, the services running on these ports, and the type of device that is being scanned. This information can be used for both legitimate and malicious purposes.

### Types of Port Scans:

**TCP Scans:**

**_SYN Scan:_** Also known as a "half-open scan", it involves sending a SYN packet (a request to start a TCP conversation) and waiting for a response. If a SYN-ACK is received, the port is open; if a RST (reset) packet is received, the port is closed.
**_Connect Scan:_** This involves attempting to fully establish a TCP connection with each port. It provides reliable results but is more likely to be detected by security systems.

**UDP Scans:**

UDP scanning is trickier since UDP (being a connectionless protocol) does not respond to probes with the same kind of acknowledgments as TCP. It's often determined that a port is open if there's no ICMP port unreachable error returned.
Techniques and Ethics:
Stealth and Speed: Various techniques are employed to perform port scans stealthily and quickly to avoid detection by network security.
Ethical Considerations: Unauthorized port scanning can be considered a hostile or invasive act because it can be a precursor to more serious cyber attacks. It's essential to have explicit permission before scanning a network.
Tools for Port Scanning:
There are many tools available for port scanning, with Nmap being one of the most popular and powerful. It offers a wide range of features and techniques for scanning network infrastructures.
Usage in Security:
Legitimate Uses: Network administrators and security professionals use port scanning to audit network security, identify vulnerabilities, and enforce security policies.
Malicious Uses: Attackers may use port scanning to identify potential attack vectors in a target’s network infrastructure.
Conclusion:
Port scanning is a powerful technique in network management and security testing. However, it should always be used responsibly and legally, with consideration for privacy and security policies.
