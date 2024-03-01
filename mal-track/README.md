# Mal Track - Malware Eradication Tool

## Description

Mal Track is a tool designed to detect and eradicate malware in a Windows environment. It terminates suspicious processes, removes them from the system startup, cleans the virtual machine of malware, and identifies the IP addresses of the attackers.

## Features

### Malware Process Detection and Termination

- **Comprehensive Scanning**: Mal Track scans system processes in real time, comparing them against known malware signatures and behaviors to accurately identify malicious activities.
- **Immediate Response**: Upon detection of a malware process, the tool promptly terminates it, effectively stopping the malware from continuing its malicious operations.
- **Safe Termination**: The tool ensures that the termination of processes does not affect system stability and preserves user data integrity.

### Removal of Malicious Programs from System Startup

- **Startup Audit**: Mal Track reviews all programs set to run at system startup, flagging those that are identified as malware.
- **Prevention of Recurrence**: It prevents malware from automatically re-launching by removing their entries from startup lists in the Windows registry and startup folders.
- **System Integrity Restoration**: By cleansing the startup routine, Mal Track aids in restoring the system's integrity and performance.

### Cleanup of Malicious Files and Registry Entries

- **Deep Cleaning**: The tool conducts a thorough search for files and registry entries related to the detected malware, ensuring no remnants are left behind.
- **Secure Deletion**: Mal Track safely removes malicious files and cleans up associated registry entries without affecting non-malicious files and system stability.
- **Restoration of System Settings**: It reverses any changes the malware may have made to system settings and registry values.

### Identification and Display of Attacker IP Addresses

- **Network Analysis**: Mal Track analyzes network traffic and logs to extract IP addresses that may be associated with the attacker or command-and-control servers.
- **Intelligence Gathering**: The tool compiles a report of potential attacker IP addresses, providing valuable information for further investigation or legal action.
- **Incident Response Support**: By identifying the source of the attack, Mal Track supports broader incident response and cybersecurity efforts to prevent future attacks.

## Prerequisites

- A Windows-based virtual machine.
- Python 3.x installed and added to the system path.

## Installation

Clone the repository using Git:
git clone https://01.kood.tech/git/Catharin/mal-track.git

Navigate to the project directory:
cd mal_track

## Usage

Run the script from the command line with administrator privileges:
python mal_track.py

## Configuration

Modify the constants at the beginning of the script to specify the parameters of the malware, such as `MalwareName`, if necessary.

## Important Notes

- Use this tool only in a controlled and secure environment.
- Do not run the tool on a production machine or network, as it could unintentionally delete important files.
- Always test the tool in a separate virtual machine before using it in an operational environment.

## Authors

- Catharin
