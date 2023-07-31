import time
import serial

from usb_select import *

def translate_resp(Line):

    if "通讯波特率设置成功" in Line :
        print("   Baud Rate set successfully")
        return

    if "波特率" in Line :
        print(">> Baud Rate: " + Line[4:])
        return

    if "传输速率设置成功" in Line :
        print("   Transmit Rate set successfully")
        return

    if "发射功率" in Line :
        print(">> Transmit Power: " + Line[5:])
        return

    if "通讯频率设置成功" in Line :
        print("   Transmit Freq. set successfully")
        return

    if "通讯频率" in Line :
        print(">> Transmit Freq.: " + Line[5:])
        return

    if "地址设置成功" in Line :
        print("   RXA set successfully")
        return

    if "本地接收地址0" in Line :
        print(">> RXA 0: " + Line[7:])
        return

    if "地址设置成功" in Line :
        print("   TXA set successfully")
        return

    if "目标地址" in Line :
        print(">> TXA: " + Line[6:])
        return


def translate_config(ser):

    Lines = []

    ser.write("AT?".encode('gb18030'))
    time.sleep(0.3)

    while ser.inWaiting() > 0:
        Lines.append(ser.readline().decode('gb18030').rstrip("\n"))

    for line in Lines:

        if 'OK' in line :
            print("OK")
            continue

        if '系统信息' in line :
            print("System Message")
            continue

        if '波特率' in line :
            print("  Baud Rate: " + line[4:])
            continue

        if '目标地址' in line :
            print("  TXA: Target address:\t" + line[10:])
            continue

        if '本地接收地址0' in line :
            print("  RXA: Local address 0\t" + line[8:])
            continue

        if '通讯频率' in line :
            print("  Frequency: " + line[5:])
            continue

        if '校验模式' in line :
            print("  CRC encoding: " + line[5:7] + "-Bit CRC")
            continue

        if '发射功率' in line :
            print("  TX Power: " + line[5:])
            continue

        if '空中传输速率' in line :
            print("  TX Rate: " + line[7:])
            continue

        if '低噪声放大增益：' in line :
            if '开启' in  line[8:] :
                state = "ON"
            else:
                state = "OFF"
            print("  LNA Gain: " + state)
            continue

if __name__ == "__main__":

    Port = port_selector()
    if Port == None :
        print("Error: not ports found")
        exit()

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
