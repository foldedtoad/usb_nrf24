import sys
sys.dont_write_bytecode = True

import time
import serial

from usb_select import *
from translate import *

def main():

    Name   = "sender"
    RXA    = "0XAA,0XBB,0XCC,0XDD,0XEE"
    TXA    = "0X11,0X22,0X33,0X44,0X55"
    #RXA    = "0X34,0X43,0X10,0X10,0X02"
    #TXA    = "0X34,0X43,0X10,0X10,0X01"

    BAUD_cmd = "AT+BAUD=2\n"
    RATE_cmd = "AT+RATE=3\n"
    FREQ_cmd = "AT+FREQ=2.400G\n"    
    RXA_cmd  = "AT+RXA=" + RXA + "\n"
    TXA_cmd  = "AT+TXA=" + TXA + "\n"

    print("\nApp: " + Name)

    Port = port_selector()
    if Port == None :
        return

    # Configure the serial connections 
    ser = serial.Serial(
        port=Port,
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
    )

    ser.isOpen()

    print("===== AT commands ======")

    ser.write(BAUD_cmd.encode())
    time.sleep(0.3)
    while ser.inWaiting() > 0:
        print(ser.readline().decode('gb18030').rstrip("\n"))

    ser.write(RATE_cmd.encode())
    time.sleep(0.3)
    while ser.inWaiting() > 0:
        print(ser.readline().decode('gb18030').rstrip("\n"))

    ser.write(FREQ_cmd.encode())
    time.sleep(0.3)
    while ser.inWaiting() > 0:
        print(ser.readline().decode('gb18030').rstrip("\n"))
    
    ser.write(RXA_cmd.encode())
    time.sleep(0.3)
    while ser.inWaiting() > 0:
        print(ser.readline().decode('gb18030').rstrip("\n"))

    ser.write(TXA_cmd.encode())
    time.sleep(0.3)
    while ser.inWaiting() > 0:
        print(ser.readline().decode('gb18030').rstrip("\n"))

    print("======= config ========")

    translate_config(ser)

    print("========================")

    input("Press any key to begin")

    while 1 :
        ser.write((Name + "\n").encode())
        time.sleep(0.05)


if __name__ == "__main__":
    main()
