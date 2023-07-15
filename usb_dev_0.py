import time
import serial

Name   = "tweedledum"
Device = '/dev/ttyUSB0'

# Configure the serial connections 
ser = serial.Serial(
    port=Device,
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

ser.isOpen()

print("I'm " + Name + "on " + Device)


#====================================================================
ser.write("AT+BAUD=2".encode())
time.sleep(1)
while ser.inWaiting() > 0:
    out = ser.readline()
    print(ser.readline().decode('gb18030'))

ser.write("AT+RATE=3".encode())
time.sleep(1)
while ser.inWaiting() > 0:
    out = ser.readline()
    print(ser.readline().decode('gb18030'))

ser.write("AT+RXA=0XE7,0XE7,0XE7,0XE7,0XE7".encode())
time.sleep(1)
while ser.inWaiting() > 0:
    out = ser.readline()
    print(ser.readline().decode('gb18030'))

ser.write("AT+TXA=0XE7,0XE7,0XE7,0XE7,0XE7".encode())
time.sleep(1)
while ser.inWaiting() > 0:
    out = ser.readline()
    print(ser.readline().decode('gb18030'))

print("========================")

#====================================================================

while 1 :
    ser.write((Name+"\n").encode())
    out = ''
    time.sleep(1)
    poll = ser.inWaiting()
    while poll > 0:
        out = ser.readline()
        if out != '':
            print(out)
