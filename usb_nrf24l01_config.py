import time
import serial

info = "AT?"
baud = "AT+BAUD"
rate = "AT+RATE"
freq = "AT+FREQ"
crc  = "AT+CRC"
rxa  = "AT+RXA"
txa  = "AT+TXA"

# Configure the serial connections 
ser = serial.Serial(
    port='/dev/ttyUSB0',              # for Ubuntu
    #port='/dev/cu.usbserial-144160',   # for MacOS
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

ser.isOpen()

while 1 :
    ser.write("AT?".encode())
    out = ''
    # Wait one second before reading output 
    # (let's give device time to answer)
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
        