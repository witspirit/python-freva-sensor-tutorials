import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
TRIG = 23
ECHO = 24

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print('Waiting a few seconds for the sensor to settle')
time.sleep(2)

scan_start = time.time()
iteration = 0
while time.time() - scan_start < 60: # Scan for 1 minute
    print('iteration ', iteration)
    iteration = iteration + 1 
    
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
    
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17165
    distance = round(distance, 1)
    print('Distance: ', distance, 'cm')
    # Avoid continous scanning
    time.sleep(0.5)
    
GPIO.cleanup()
