# Injector

## Description

This Python script, binder.py, is designed to take two executable binary files, convert them to a Base64 string representation, and then run each executable in a temporary space.

## Audit questions

https://github.com/01-edu/public/tree/master/subjects/cybersecurity/injector/audit

## Requirements

- Python 3.x
- Access to a Unix-like terminal or command prompt
- Two binary files that you wish to bind and execute

## Usage

To use this script, you should have two binary files that you want to execute sequentially. The script takes the path to these files as command-line arguments.

To better demonstrate the capabilities of this program, there are three folders with files, each written in a different programming language: C, Python, and Go.

- Compile the Go file into a binary file using the command: `go build go/main.go`

- Compile the C file using the following command `gcc ./C/main.c -o c-file`.

- To compile the Python file, first install Pyinstaller `pip install pyinstaller`
  and then compile the file using the command `pyinstaller --onefile ./python/hello.py`.

Here is the syntax for using binder.py:
`python binder.py path/to/binary1 path/to/binary2`
You can choose two of files, for example:
`python binder.py main c-file`
or `python binder.py c-file ./dist/hello`

## How It Works

The script operates in the following manner:

- It reads the content of the binaries you provide as arguments.
- It converts the binary data into a Base64 string to handle it safely within the script.
- It then creates a temporary file, writes the decoded Base64 content into this file, and makes the file executable.
- The script executes the temporary file.
- This process is repeated for both of the binary files provided as arguments.

## Author

Catharin
