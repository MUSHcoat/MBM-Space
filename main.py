import time
import os
from bme280 import BME
from mq9 import MQ

# define sensors
BME = BME(decimal=5)
MQ = MQ()

#!!!!!!!!!!!!! TO BE DELETED !!!!!!!!!!!!!!!!
iteration = 0

if __name__ == '__main__':
    while True:
        os.system('clear')
        
        print(f'buna ziua, iteratia {iteration}')
        print(f'Temperature: {BME.temp()}')
        print(f'Humidity: {BME.hum()}')
        print(f'Pressure: {BME.pres()}')
        print(f'Altitude: {BME.alt()}')
        
        print('\n')
        
        print(f'Value: {MQ.value()}')
        print(f'Voltage: {MQ.voltage()}')

        iteration += 1
        time.sleep(1)
