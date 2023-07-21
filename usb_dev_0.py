import time
import serial

Name   = "tweedledum"
Device = "/dev/ttyUSB0"
RXA    = "0X11,0X22,0X33,0X44,0X55"
TXA    = "0XAA,0XBB,0XCC,0XDD,0XEE"

BAUD_cmd = "AT+BAUD=2\n"
RATE_cmd = "AT+RATE=3\n"
RXA_cmd  = "AT+RXA=" + RXA + "\n"
TXA_cmd  = "AT+TXA=" + TXA + "\n"

# Configure the serial connections 
ser = serial.Serial(
    port=Device,
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

ser.isOpen()

print("\n" + Name + " on " + Device)
print("RXA: " + RXA)
print("TXA: " + TXA)

ser.write(BAUD_cmd.encode())
ser.write(RATE_cmd.encode())
ser.write(RXA_cmd.encode())
ser.write(TXA_cmd.encode())

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
