import openpyxl
import platform
import socket
import ctypes

def gather_computer_info():
    # Ваш код для сбора информации о компьютере
    info = {
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
    return info

def create_excel(computer_info, filename='output.xlsx'):
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    # Запись заголовка
    sheet['A1'] = 'Отчет о компьютере'

    # Запись данных о компьютере
    row = 3
    for key, value in computer_info.items():
        sheet[f'A{row}'] = key
        sheet[f'B{row}'] = value
        row += 1

    # Сохранение Excel-файла
    workbook.save(filename)

# Сбор информации о компьютере
computer_info = gather_computer_info()

# Создание Excel-файла
create_excel(computer_info, filename='output.xlsx')