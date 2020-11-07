# iot-bi-tfg

Applications to connect humidity and temperature sensor DHT11 to a Raspberry Pi.

## Needed software
- Python and compilers libraries

  sudo apt-get install build-essential python dev

- Git library to download the code from GitHub

  sudo apt-get install git

- Circuit Python library from Adafruit https://github.com/adafruit/Adafruit_CircuitPython_DHT

  git clone https://github.com/adafruit/Adafruit_Python_DHT.git && cd Adafruit_Python_DHT && sudo python setup.py install

## Connection diagram
![alt text](https://github.com/vga85/iot-bi-tfg/blob/main/raspberry_pi_model_b_bb.png)

## Configuration & Installation

- link to TFG

## Execution
For local execution:

  sudo dht_cli.py

To send data to Power BI in background

  sudo dht_powerbi.py &

## Questions and suggestions
vgonzalezalv@uoc.edu
