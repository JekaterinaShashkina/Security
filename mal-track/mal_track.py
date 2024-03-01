import os
import subprocess
import re
import winreg as reg

MalwareName = "mal-track.exe"
IPRegex = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
RegPaths = [
    (reg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Run"),
    (reg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\RunOnce"),
    (reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run"),
    (reg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\RunOnce"),
]

def get_process_pid(name):
    try:
        output = subprocess.check_output(['tasklist', '/FI', f"IMAGENAME eq {name}", '/FO', 'CSV'], text=True)
        lines = output.strip().split('\n')
        if len(lines) > 1:
            pid = int(lines[1].split(",")[1].strip('"'))
            return pid
    except Exception as e:
        print(e)
    return 0

def get_ips_from_file(file_path):
    ip_set = set()
    try:
        with open(file_path, 'r') as file:
            for line in file:
                ips = re.findall(IPRegex, line)
                ip_set.update(ips)
    except Exception as e:
        print(e)
    return ip_set

def kill_process(pid):
    if pid == 0:
        return
    try:
        subprocess.run(['taskkill', '/F', '/PID', str(pid)], check=True)
    except Exception as e:
        print(e)

def delete_registry_keys(name):
    for hkey, path in RegPaths:
        try:
            with reg.OpenKey(hkey, path, 0, reg.KEY_ALL_ACCESS) as key:
                i = 0
                while True:
                    try:
                        value_name, value_data, _ = reg.EnumValue(key, i)
                        if name.lower() in value_data.lower():
                            print(f"{value_name} was found hiding in {path}\\{value_name}")
                            reg.DeleteValue(key, value_name)
                            print(f"{value_name} removed the virus from start-up.")
                    except OSError:
                        break
                    i += 1
        except Exception as e:
            print(e)

def main():
    pid = get_process_pid(MalwareName)
    if pid != 0:
        try:
            output = subprocess.check_output(['wmic', 'process', 'where', f"ProcessId={pid}", 'get', 'ExecutablePath'], text=True)
            lines = output.strip().split('\n')
            if len(lines) > 1:
                path = lines[1].strip()
                ips = get_ips_from_file(path)
                if ips:
                    print(f"Process '{MalwareName}' IP: {', '.join(ips)}")
                else:
                    print(f"No IP for {MalwareName} found in {path}")
        except Exception as e:
            print(e)
        kill_process(pid)
    else:
        print(f"{MalwareName} process not found")
    delete_registry_keys(MalwareName)

if __name__ == "__main__":
    main()
