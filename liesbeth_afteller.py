import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LED = 21
ledState = True
GPIO.setup(LED, GPIO.OUT)

afteller = 5
while afteller >= 1:
    print(afteller)
    GPIO.output(LED,True)
    time.sleep(afteller)
    GPIO.output(LED,False)
    time.sleep(0.5)
    afteller = afteller - 1
    
GPIO.output(LED,True)
print('BOOM!')
time.sleep(0.5)
GPIO.output(LED,False)