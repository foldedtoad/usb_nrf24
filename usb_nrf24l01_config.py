import time
import serial

Device = '/dev/ttyUSB0'
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

print("\nUsing: " + Device)
print("RXA: " + RXA)
print("TXA: " + TXA)

print("========================")

ser.write(BAUD_cmd.encode('gb18030'))
ser.write(RATE_cmd.encode('gb18030'))

ser.write(RXA_cmd.encode('gb18030'))
time.sleep(1)
while ser.inWaiting() > 0:
    print(ser.read_until().decode('gb18030'))
    print(ser.read_until().decode('gb18030'))

print("======================== RXA ")

ser.write(TXA_cmd.encode('gb18030'))
time.sleep(1)
while ser.inWaiting() > 0:
    line = ser.read_until()
    header = '地址设置成功！'.encode('gb18030')
    if header.decode('gb18030') in line.decode('gb18030') :
        print("The address is set successfully!")

    line = ser.read_until()
    header = '目标地址'.encode('gb18030')
    if header.decode('gb18030') in line.decode('gb18030') :
        print("RX Address: " + line[12:].decode('gb18030'))

print("======================== TXA ")

ser.write("AT?".encode())
out = ''
time.sleep(1)
while ser.inWaiting() > 0:
    out = ser.readline()
    print(ser.readline().decode('gb18030'))

print("========================")


'''
AT Commands

System info : AT?

Baudrate : AT+BAUD=n where n = 1-6 
                1:4800,
                2:9600,
                3:14400,
                4:19200,
                5:38400,
                6:115200
                (default 9600Kbps)

NRF Rate : AT+RATE=n where n = 1-3 
                1:250K,
                2:1M,
                3:2M
                (default 2Mbps)

Local Address : AT+RXA=0Xnn,0Xnn,0Xnn,0Xnn,0Xnn 
                where nn are the local receiving address 
                (default 0xff,0xff,0xff,0xff,0xff)

Target Address : AT+TXA=0Xnn,0Xnn,0Xnn,0Xnn,0Xnn
                where nn are the target address

Operating Freq. : AT+FREQ=2.nnnG
                where nnn = 400 / 525
                (default 2.400G)

Checksum mode : AT+CRC=n 
                where n = 8 /16
                (default : 16 bit)
'''
        