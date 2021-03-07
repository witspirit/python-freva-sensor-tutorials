import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PIR_PIN = 23
GPIO.setup(PIR_PIN, GPIO.IN)

print('Starting up the PIR Module (click on STOP to exit)')
time.sleep(1)
print('Ready')

while True:
    #if GPIO.input(PIR_PIN):
    #    print(time.time(), ' Motion Detected')
    print(round(time.time(),0), 'Motion = ', GPIO.input(PIR_PIN))
    time.sleep(1)
