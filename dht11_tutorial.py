import Adafruit_DHT
sensor = Adafruit_DHT.DHT11
DHT11_pin = 23

humidity, temperature = Adafruit_DHT.read_retry(sensor, DHT11_pin)
print(humidity, temperature)
if humidity is not None and temperature is not None:
    print('Temperature={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading from the sensor. Try again!')
# Never got any succesful reading... Not sure why
# Also had to run it command line using sudo python3 dht11_tutorial.py to avoid an error regarding access to GPIO

