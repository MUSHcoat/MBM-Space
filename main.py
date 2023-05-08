import time
import os
import board
import busio
import adafruit_ads1x15.ads1115 as ADS

from bme280 import BME
from mq9 import MQ
from gp2y import GP2Y



#general defintions
i2c = busio.I2C(board.SCL, board.SDA)

pin_led = 12
pin_vo = 40
pin_vled = 38
        
# define sensors
BME = BME(decimal=5)
#MQ = MQ(i2c)
MQ = None
GP2Y = GP2Y(i2c)

#debug
iteration = 0

if __name__ == '__main__':
    while True:
        os.system('clear')
        
        if BME is not None:
                print(f'buna ziua, iteratia {iteration}')
                print(f'Temperature: {BME.temp()}')
                print(f'Humidity: {BME.hum()}')
                print(f'Pressure: {BME.pres()}')
                print(f'Altitude: {BME.alt()}')
                print('')
        
        if MQ is not None:
                print(f'Value: {MQ.value()}')
                print(f'Voltage: {MQ.voltage()}')
                print('')
        
        if GP2Y is not None:
                print(f'Dust: {GP2Y.read()} mg/m3')
                print('')

        iteration += 1
        time.sleep(1)
