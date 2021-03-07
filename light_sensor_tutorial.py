import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
LIGHT = 23
GPIO.setup(LIGHT, GPIO.IN)
lOld = not GPIO.input(LIGHT)

print('Starting up the Light module (click on STOP to exit)')
time.sleep(0.5)

def showLightStatus():
    if GPIO.input(LIGHT):
        print('\u263e')
    else:
        print('\u263c')

while True:
    if GPIO.input(LIGHT) != lOld:
        showLightStatus()
    lOld = GPIO.input(LIGHT)
    time.sleep(0.2)

