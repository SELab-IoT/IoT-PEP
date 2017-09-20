#led
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.IN)

while True:
    in_value=GPIO.input(12)
    if in_value == False:
        print("click...")
        GPIO.output(11,False)
        time.sleep(1)
        GPIO.output(11,True)
        while in_value == False:
            in_value = GPIO.input(12)

