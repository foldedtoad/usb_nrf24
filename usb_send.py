import time
import serial

Name = "sender"
Device = '/dev/ttyUSB1'
RXA    = "0XAA,0XBB,0XCC,0XDD,0XEE"
TXA    = "0X11,0X22,0X33,0X44,0X55"

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

print("\nI'm " + Name + " on " + Device)
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
    time.sleep(0.05)