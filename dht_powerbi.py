#  Read humidity and temperature values from DHTxx sensor and
#  send data to Power BI streaming dataset
#
#  Adafruit DHT library:
#  https://github.com/adafruit/Adafruit_Python_DHT
#
#  Based on examples by Sirui Sun
#
# Author : Vicente Gonzalez
# Date   : 06/11/2020
#
# 

# Importing needing libraries
import urllib3, time
from datetime import datetime
import Adafruit_DHT

# We define the type of sensor. Change to DHT22 if you use this type of DHT-sensor.
sensor = Adafruit_DHT.DHT11 
#sensor = Adafruit_DHT.DHT22

# pin which reads the temperature and humidity from sensor GPIO port (OUT)
gpio = 17         

# REST API endpoint, given to you when you create an API streaming dataset
# Will be of the format: https://api.powerbi.com/beta/<tenant id>/datasets/< dataset id>/rows?key=<key id>
REST_API_URL = 'https://api.powerbi.com/beta/aec762e4-3d54-495e-a8fe-4287dce6fe69/datasets/3f8a8652-9348-4a0e-8269-657107031bb0/rows?noSignUpCheck=1&key=kNRO6B8sLBvjAm1VIyasCWutvy83omGZGUQdBHUK%2B0CqoVnoXIrioOMtrewuARyfq8xCB4n6YAu8Iqhy8Hceog%3D%3D'

# Gather temperature and sensor data and push to Power BI REST API
while True:
    try:
        # read and print humidity and temperature values from sensor
        humidity,temperature = Adafruit_DHT.read_retry(sensor, gpio)
        #print ("Temp={0:0.1f}*C Humidity={1:0.1f}%".format(temperature, humidity))
        
        # ensure that timestamp string is formatted properly
        now = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S%Z")
    
        # data that we're sending to Power BI REST API
        data = '[{{ "timestamp": "{0}", "temperature": {1:0.1f}, "humidity": {2:0.1f} }}]'.format(now, temperature, humidity)
        print (data)
        # make HTTP POST request to Power BI REST API
        http = urllib3.PoolManager()
        req = http.request('POST',REST_API_URL, body=data, headers={'Content-Type':'text/html'})
        response = req.read()
        print("POST request to Power BI with data:{0}".format(data))
        print("Response: HTTP {0} {1}\n".format(response, response))   
    
        time.sleep(15)
        
        #Capture exceptions
    except urllib3.exceptions.HTTPError as e:
        print("HTTP Error: {0} - {1}".format(e.code, e.reason))
    except urllib3.exceptions.RequestError as e:
        print("Request Error: {0}".format(e.reason))
    except Exception as e:
        print("General Exception: {0}".format(e))