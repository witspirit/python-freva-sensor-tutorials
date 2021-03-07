import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LED = 21
ledState = True
GPIO.setup(LED, GPIO.OUT)

afteller = 2.0
while afteller >= 0.001:
    print(afteller)
    GPIO.output(LED,True)
    time.sleep(afteller)
    GPIO.output(LED,False)
    time.sleep(0.2)
    afteller = afteller / 2
    
herhalen = 100    
while herhalen > 0:
    GPIO.output(LED,True)
    time.sleep(0.05)
    GPIO.output(LED,False)
    time.sleep(0.1)
    herhalen = herhalen - 1

GPIO.output(LED,False)

