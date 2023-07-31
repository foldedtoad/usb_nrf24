import sys
sys.dont_write_bytecode = True

import time
import serial

from usb_select import *
from translate import *

def display_config() :

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
    
    print("\nUsing: " + Port)
    
    print("======= config ========")
    
    translate_config(ser)

    print("========================")
   

if __name__ == "__main__":
    display_config()
