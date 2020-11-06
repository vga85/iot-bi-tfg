#  Adafruit DHT library:
#  https://github.com/adafruit/Adafruit_Python_DHT
#
#  Based on examples by Tony DiCola
#
# Author : Vicente Gonzalez
# Date   : 06/11/2020
#
# 

#import Adafruit Library
import Adafruit_DHT
import time

# We define the type of sensor. Change to DHT22 if you use this type of DHT-sensor.
sensor = Adafruit_DHT.DHT11
# Where OUT pin is connected to Raspberry Pi
gpio = 17

while True:
    #Reading the sensor
    humidity, temperature = Adafruit_DHT.read(sensor, gpio)
    #if we get a reading value from the sensor
    if humidity is not None and temperature is not None:
    #printing the results on the screen
        print("Temp={0:0.1f}C  Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Sensor failure. Check wiring.");
    #Receiving values every 60 seconds
    time.sleep(10);