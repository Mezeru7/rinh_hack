from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import platform
import socket
import subprocess
import ctypes


def audit():
    # Cбор информации о компьютере
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


def create(pcinfo, filename='output.pdf'):
    # Создание PDF-файла
    pdf = canvas.Canvas(filename, pagesize=letter)

    pdf.drawString(100, 750, 'Computer information')

    y_position = 730
    for key, value in pcinfo.items():
        y_position -= 15
        pdf.drawString(100, y_position, f'{key}: {value}')

    pdf.save()

pcinfo = audit()

create(pcinfo, filename='output.pdf')
