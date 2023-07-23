import time
import serial

Name = "sender"
Device = '/dev/ttyUSB1'
RXA    = "0XAA,0XBB,0XCC,0XDD,0XEE"
TXA    = "0X11,0X22,0X33,0X44,0X55"

BAUD_cmd = "AT+BAUD=2"
RATE_cmd = "AT+RATE=3"
RXA_cmd  = "AT+RXA=" + RXA
TXA_cmd  = "AT+TXA=" + TXA

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
#'''
ser.write(BAUD_cmd.encode())
time.sleep(0.3)
line = ser.read_until().decode('gb18030')
ser.write(RATE_cmd.encode())
time.sleep(0.3)
line = ser.read_until().decode('gb18030')
ser.write(RXA_cmd.encode())
time.sleep(0.3)
line = ser.read_until().decode('gb18030')
ser.write(TXA_cmd.encode())
time.sleep(0.3)
line = ser.read_until().decode('gb18030')
#'''
print("========================")

#'''
ser.write("AT?".encode('gb18030'))
time.sleep(0.3)
while ser.inWaiting() > 0:
    line = ser.read_until()
    print(line.decode('gb18030'))

print("========================")
#'''

while 1 :
    ser.write((Name + "\n").encode())
    time.sleep(0.05)
