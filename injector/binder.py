import base64
import subprocess
import sys
import os
import tempfile

def file_to_base64_string(file_path):
    with open(file_path, 'rb') as file:
        binary_data = file.read()
    return base64.b64encode(binary_data).decode('utf-8')

def run_executable(binary_data):
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(base64.b64decode(binary_data))
        tmp_file.flush()  # Сохраняем изменения
        os.chmod(tmp_file.name, 0o755)  # Даем права на выполнение
        subprocess.run(tmp_file.name)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python binder.py <filename1> <filename2>")
        sys.exit(1)

    file1, file2 = sys.argv[1], sys.argv[2]
    file1_string = file_to_base64_string(file1)
    file2_string = file_to_base64_string(file2)

    run_executable(file1_string)
    run_executable(file2_string)
