#define RXD 14 porta 10
#define TXD    porta 08


import serial
ser=Serial.Serial (port= '/dev/ttyS3',
                     baudrate=9600, parity=Serial. PARITY_NONE,
                     stopbits=Serial.STOPBITS_ONE,
                     bytesize= Serial.EIGHTBITS,
                     timeout=1
                      )

while 1:
    x= ser.readLine()
    if len(x)> 0:
        print("Código RFID é:",x.hex())