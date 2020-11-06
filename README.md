# iot-bi-tfg

Applications to connect humidity and temperature sensor DHT11 to a Raspberry Pi.

## Needed software
- Python and compilers libraries

  sudo apt-get install build-essential python-dev

- Git library to download the code from GitHub

  sudo apt-get install git

- Circuit Python library from Adafruit https://github.com/adafruit/Adafruit_CircuitPython_DHT

  git clone http://github.com/adafruit/Adafruit_Python_DHT.git
  cd Adafruit_Python_DHT
  sudo python setup.py install

## Diagrama de conexión
![](https://uoc0-my.sharepoint.com/:i:/g/personal/vgonzalezalv_uoc_edu/EWwsiIxEL39Cj5mkklrk-iwBzzCpxwZmXAVa2vSfNKa_Mw?e=zf68P3)

## Configuration & Installation

- link to TFG

## Execution
For local execution:

  sudo dht_cli.py

To send data to Power BI

  sudo dht_powerbi.py

## Questions & Suggestions
vgonzalezalv@uoc.edu