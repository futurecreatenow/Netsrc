import serial

ser = serial.Serial("COM1",9600)
print(ser.name)

ser.write(b'terada')

ser.close()
