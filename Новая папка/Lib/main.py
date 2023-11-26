import platform
import socket
import subprocess
import ctypes
import psutil


def start(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True,encoding='cp866' )
    return result.stdout.strip()


def allinfo():
    interface = {
        "System Information": start("systeminfo"),
        "Active Setup": start("reg query HKLM\\SOFTWARE\\Microsoft\\Active Setup\\Installed Components /s"),
        "Installed Programs": start("wmic product get name,version"),
    }
    return interface


def maininfo():
    systeminfa = {
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
    return systeminfa


def netinfo():
    inetinfo = psutil.net_if_addrs()
    return inetinfo


def gethw():
    pass


def getdevice():
    pass


def main():
    systeminterface = allinfo()
    systeminfo = maininfo()
    networkinfo = netinfo()
    hwinfo = gethw()
    dmmeneger = getdevice()

    print("Обзор системы:")
    for section, info in systeminterface.items():  # Заменил system_overview на systeminterface
        print(f"{section}:\n{info}\n")

    print("\nИнформация о системе:")
    for key, value in systeminfo.items():
        print(f"{key}: {value}")

    print("\nСетевая информация:")
    for interface, addrs in networkinfo.items():
        print(f"Интерфейс: {interface}")
        for addr in addrs:
            print(
                f"  Семейство адресов: {addr.family}, Адрес: {addr.address}, Маска подсети: {addr.netmask}, Широковещательный IP: {addr.broadcast}")
        print()
if __name__ == "__main__":
    main()
