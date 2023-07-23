# nRF24l01-USB-Adapter-V2.0 Documents

This directory contains various documents and notes.  
Some are in Chinese and some are in English.  
  
The Chinese-to-English translation was preformed with Google Translate, so beware.

---

# AT Commands

**System Info**  
Cmd: AT?  
Returns current nRF24L01's configuration.

**Baud Rate**  
Cmd: AT+BAUD=n   
Where n = 1-6  
- 1=4800,  
- 2=9600,  
- 3=14400,  
- 4=19200,  
- 5=38400,  
- 6=115200  
(default 9600 Kbps)  
  
**NRF Rate**  
Cmd: AT+RATE=n   
Where n = 1-3    
- 1:250K,  
- 2:1M,  
- 3:2M  
(default 2Mbps)  
  
**Local Address**  
Cmd: AT+RXA=0Xnn,0Xnn,0Xnn,0Xnn,0Xnn   
Where nn are the local receiving address in hex     
(default 0xFF,0xFF,0xFF,0xFF,0xFF)

**Target Address**  
Cmd: AT+TXA=0Xnn,0Xnn,0Xnn,0Xnn,0Xnn  
Where nn are the target address  

**Operating Freq.**  
Cmd: AT+FREQ=2.nnnG  
Where nnn = 400 / 525  
(default 2.400G)

**Checksum Mode**  
Cmd: AT+CRC=n   
Where n = 8 /16  
(default : 16 bit)        
