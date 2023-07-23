import time
import serial

Device = '/dev/ttyUSB1'
RXA    = "0XAA,0XBB,0XCC,0XDD,0XEE"
TXA    = "0X11,0X22,0X33,0X44,0X55"

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

print("\nUsing: " + Device)
print("RXA: " + RXA)
print("TXA: " + TXA)

print("========================")

'''
ser.write(TXA_cmd.encode('gb18030'))
time.sleep(1)
while ser.inWaiting() > 0:
    line = ser.read_until()
    header = '地址设置成功！'.encode('gb18030')
    if header.decode('gb18030') in line.decode('gb18030') :
        print("The address is set successfully!\n")

    line = ser.read_until()
    header = '目标地址'.encode('gb18030')
    if header.decode('gb18030') in line.decode('gb18030') :
        print("RX Address: " + line[12:].decode('gb18030'))

print("========================")
'''

ser.write("AT?".encode('gb18030'))
time.sleep(0.3)
while ser.inWaiting() > 0:
    line = ser.read_until()
    print(line.decode('gb18030'))

print("========================")
