import platform
import socket
import subprocess
import ctypes

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding='cp866')
    return result.stdout.strip()

def get_system_overview():
    overview = {
        "System Information": run_command("systeminfo"),
        "Active Setup": run_command("reg query HKLM\\SOFTWARE\\Microsoft\\Active Setup\\Installed Components /s"),
        "Installed Programs": run_command("wmic product get name,version"),
    }
    return overview

def get_system_info():
    system_info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "OS Release": platform.release(),
        "Architecture": platform.architecture(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "Hostname": socket.gethostname(),
        "IP Address": socket.gethostbyname(socket.gethostname()),
        "User Privileges": ctypes.windll.shell32.IsUserAnAdmin(),
    }
    return system_info

def get_network_info():
    pass

def get_hardware_info():
    pass

def get_device_manager_info():
    pass

def main():
    system_overview = get_system_overview()
    system_info = get_system_info()
    network_info = get_network_info()
    hardware_info = get_hardware_info()
    device_manager_info = get_device_manager_info()

    print("System Overview:")
    for section, info in system_overview.items():
        print(f"{section}:\n{info}\n")

    print("\nSystem Information:")
    for key, value in system_info.items():
        print(f"{key}: {value}")
if __name__ == "__main__":
    main()
