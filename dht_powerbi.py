"""
Python sample for Raspberry Pi which reads temperature and humidity values from
a DHT11 sensor, and sends that data to Power BI for use in a streaming dataset.
"""

import urllib3, time
from datetime import datetime
import Adafruit_DHT as dht

# type of sensor that we're using
SENSOR = dht.DHT11  

# pin which reads the temperature and humidity from sensor GPIO port
PIN = 17         

# REST API endpoint, given to you when you create an API streaming dataset
# Will be of the format: https://api.powerbi.com/beta/<tenant id>/datasets/< dataset id>/rows?key=<key id>
REST_API_URL = 'https://api.powerbi.com/beta/aec762e4-3d54-495e-a8fe-4287dce6fe69/datasets/6f2f8db8-6aff-420e-aa3b-a255debe33d8/rows?noSignUpCheck=1&key=ws0lnS9yrp%2F%2FlMGsVKtizZgl%2BagEM%2Bzar2c21fWkkJewESOp4iffwp03LvzlCFNZWUMYFRp0SDictwNu%2FRUJNg%3D%3D'

# Gather temperature and sensor data and push to Power BI REST API
while True:
    try:
        # read and print humidity and temperature values from sensor
        humidity,temp = dht.read_retry(SENSOR, PIN)
        #print 'Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temp, humidity)
        
        # ensure that timestamp string is formatted properly
        now = datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S%Z")
    
        # data that we're sending to Power BI REST API
        data = '[{{ "timestamp": "{0}", "temperature": {1:0.1f}, "humidity": {2:0.1f} }}]'.format(now, temp, humidity)
        print (data)
        # make HTTP POST request to Power BI REST API
        http = urllib3.PoolManager()
        req = http.request('POST',REST_API_URL, body=data, headers={'Content-Type':'text/html'})
        response = req.read()
        print("POST request to Power BI with data:{0}".format(data))
        print("Response: HTTP {0} {1}\n".format(response, response))   
    
        time.sleep(1)
        
        #Capture exceptions
    except urllib3.exceptions.HTTPError as e:
        print("HTTP Error: {0} - {1}".format(e.code, e.reason))
    except urllib3.exceptions.RequestError as e:
        print("Request Error: {0}".format(e.reason))
    except Exception as e:
        print("General Exception: {0}".format(e))