import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
SIMPLE_DETECTOR = 23
LINEAR_DETECTOR = 21
REED_DETECTOR = 16
GPIO.setup(SIMPLE_DETECTOR, GPIO.IN)
GPIO.setup(LINEAR_DETECTOR, GPIO.IN)
GPIO.setup(REED_DETECTOR, GPIO.IN)

selectedDetector = SIMPLE_DETECTOR

lastDetection = not GPIO.input(selectedDetector)
while True:
    currentDetection = GPIO.input(selectedDetector)
    if currentDetection != lastDetection:
        print(round(time.time(),0),' Change detected: ', currentDetection)
        lastDetection = currentDetection    
    time.sleep(0.01)

