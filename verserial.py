import serial
#com0com、teratermを使用
ser = serial.Serial("COM1",9600)
print(ser.name)

ser.write(b'terada')

ser.close()
