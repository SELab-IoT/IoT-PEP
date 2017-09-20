import serial
s = serial.Serial(port='/dev/tty.ENTITY1-DevB', baudrate=9600)

s.write(('{"led":1,"time":1000}').encode())