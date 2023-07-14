import serial
from serial.tools import list_ports

enmu_ports = enumerate(list_ports.comports())
port = ""

for n, (p, descriptor, hid) in enmu_ports:
    print(p, descriptor, hid)
