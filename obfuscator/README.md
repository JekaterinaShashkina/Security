# Obfuscator

## Objective

The goal of this project is to understand polymorphic encryption. Principle used by computer virus developers to change the signature of their programs.

## Audit questions

https://github.com/01-edu/public/blob/master/subjects/cybersecurity/obfuscator/audit/README.md

Link for video demo
https://youtu.be/bM26nrQSkGU

## Description

This project demonstrates the creation of a simple reverse SSH shell using Python. A reverse SSH shell allows for remote system management: the server initiates a connection to the client, after which it can send commands to be executed on the client machine. This example also showcases the dynamic modification of the client program's signature by generating a random hash each time it runs, which can be used for educational purposes to study basic principles of security and anonymity.

## Prerequisites

Python 3 is required for this project to work. Ensure it is installed on both machines (client and server). This project has been tested with Python 3.8 and above.

## Installation and Setup

### Server Setup

- Save the server code in a file named `server.py`.
- Run the server script with the command: `python server.py`

### Client Setup

- Save the client code in a file named `client.py`.
- Edit the SERVER_HOST and SERVER_PORT variables in `client.py` to specify the server's IP address and port, respectively.
- Run the client script with the command: `python client.py`

## Usage

After establishing a connection between the client and the server, you can enter commands on the server. These commands will be executed on the client, and the execution results will be sent back to the server. To end the session and disconnect the client, send the command `exit`.

Here are some examples of safe commands you can use to test the functionality of the reverse SSH shell without causing any harm or unwanted changes to the client system:

- `echo "Hello World"`: Prints "Hello World" to the terminal. This is a harmless way to ensure that commands are being transmitted and executed properly.
- `date`: Displays the current date and time on the client system. Useful for verifying real-time command execution.
- `whoami`: Shows the username of the user under which the client program is running. Helps in understanding the privilege level of the executed commands.
- `hostname`: Outputs the name of the client machine. This can confirm you're connected to the intended target.
- `ls` or `dir`: Lists files and directories in the current working directory on the client machine. This command allows you to verify access to the filesystem without making any changes.
- `uptime`: Shows how long the client system has been running since its last reboot. This provides insight into the system's stability and availability.

It's important to use commands that don't alter the system state or pose any security risk. These commands provide enough functionality to test the reverse SSH shell's operational status without modifying or potentially disrupting the client system's operation.

## Security

Do not use this project for malicious purposes.
Always obtain permission before testing on others' systems.
Use this code for learning and self-education on cybersecurity issues.

## Author

Catharin
