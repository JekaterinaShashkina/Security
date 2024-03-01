# EVASION

## Project Overview
The goal of this project is to develop a Windows program capable of encrypting another program, increasing its size by 101 MB, incrementing a specific integer value up to 100001, and after a delay of 101 seconds, checking the elapsed time before decrypting and executing the encrypted program.

## Audit questions
https://github.com/01-edu/public/tree/master/subjects/cybersecurity/evasion/audit

Link for video demo https://youtu.be/aBHMRWY7uNY

## System Requirements
Windows operating system.
Python 3.6 or higher.
Sufficient disk space for file operations (consider the file size increase of 101 MB).
Installation and Setup
Before starting, ensure that Python is installed on your machine. This can be verified by running in the command line:
`python --version`
If Python is installed, you will see the version of the interpreter. 
If not, install Python from the official website `python.org`.

## Usage
To use the program, follow the steps below:

- Copy the script to your preferred directory.
- Open a command line or terminal and navigate to the directory containing the script.
- Execute the script, passing the path to the file you wish to encrypt as a command line argument. Example:
`python evasion.py path/to/your/file`

The program will:
- Encrypt the specified file, increasing its size by 101 MB.
- Wait for 101 seconds.
- Decrypt the file and check if 101 seconds have elapsed since encryption before attempting to execute the file.

## Implementation Features
- File encryption and decryption are achieved by modifying each byte of the file using a simple algorithm for demonstration purposes.
- File size increase is accomplished by appending empty space at the end of the file.
- The time delay is implemented through time.sleep.
- Checking the time before decryption and execution demonstrates the ability to incorporate time check conditions into the logic of encryption programs.

## Additional Security Measures
Hash Comparison Before and After Encryption: To ensure the integrity and verify the modification of the file's binary data, the program includes a feature to compare the file's hash before and after encryption. This ensures that the encryption process has indeed altered the binary signature of the file, providing an additional layer of verification for the encryption integrity.

## Author
Catharin
