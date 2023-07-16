import time
import serial

Name = "tweedledee"
Device = '/dev/ttyUSB1'

# Configure the serial connections 
ser = serial.Serial(
    port=Device,
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

ser.isOpen()

print("\nI'm " + Name + " on " + Device)

ser.write("AT+BAUD=2\n".encode())
ser.write("AT+RATE=3\n".encode())
ser.write("AT+RXA=0xE7,0xE7,0xE7,0xE7,0xE7\n".encode())
ser.write("AT+TXA=0x11,0x22,0x33,0x44,0x55\n".encode())

print("========================")

count = 1

while 1 :
    ser.write((Name + "\n").encode())
    line = ''
    time.sleep(1)
    poll = ser.inWaiting()
    while poll > 0:
        line = ser.readline().decode('gb18030')
        if line != '':
            print(str(count) + ": " + line)
            count += 1