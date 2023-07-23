# nRF24l01-USB-Adapter-V2.0 Documents

This directory contains various documents and notes.  
Some are in Chinese and some are in English.  
  
The Chinese-to-English translation was preformed with Google Translate, so beware.

============================================

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

==========================================                
