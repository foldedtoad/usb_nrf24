# usb_nrf24
USB-to-nRF24L01 Dongle Project


![here](https://github.com/foldedtoad/usb_nrf24/blob/master/images/usbserial2nrf24.jpg)

Below is a screenshot showing the intraction between two devices.  
The two programs are *usb_send.py* and *usb_receive.py*.    
  
Both programs have an optional parameter, "-c".  This CLI option indicates that configuration 
is to be update to the Dongle. If the parameter is omitted, then the configuration stored in 
the Dongle flash will be used. The idea being to reduce the wear on the Dongle flash memory.
Unfortunately, this option is not visable in the screenshot below.


![here](https://github.com/foldedtoad/usb_nrf24/blob/master/images/send_receive.png)
