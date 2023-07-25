import time
import serial

from usb_select import *

def translate_config(ser):

    Lines = []

    ser.write("AT?".encode('gb18030'))
    time.sleep(0.3)

    while ser.inWaiting() > 0:
        Lines.append(ser.readline().decode('gb18030').rstrip("\n"))

    for line in Lines:

        header = 'OK'
        if header in line :
            print("OK")
            continue

        header = '系统信息：'
        if header in line :
            print("System Message")
            continue

        header = '波特率：'
        if header in line :
            print("  Baud Rate: " + line[4:])
            continue

        header = '目标地址：'
        if header in line :
            print("  TXA: Target address:\t" + line[10:])
            continue

        header = '本地接收地址0：'
        if header in line :
            print("  RXA: Local address 0\t" + line[8:])
            continue

        header = '通讯频率：'
        if header in line :
            print("  Frequency: " + line[5:])
            continue

        header = '校验模式：'
        if header in line :
            print("  CRC encoding: " + line[5:7] + "-Bit CRC")
            continue

        header = '发射功率：'
        if header in line :
            print("  TX Power: " + line[5:])
            continue

        header = '空中传输速率：'
        if header in line :
            print("  TX Rate: " + line[7:])
            continue

        header = '低噪声放大增益：'
        if header in line :
            if '开启' in  line[8:] :
                state = "ON"
            else:
                state = "OFF"
            print("  LNA Gain: " + state)
            continue

if __name__ == "__main__":

    Port = port_selector()
    if Port == None :
        pass

    # Configure the serial connections 
    ser = serial.Serial(
        port=Port,
        baudrate=9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
    )

    ser.isOpen()

    print("\nPort: " + Port)

    translate_config(ser)
