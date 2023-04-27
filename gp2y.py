import os
import time

import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

class GP2Y:
    def __init__(self):
        self.i2c = busio.I2C(board.SCL, board.SDA)
        self.ads = ADS.ADS1115(self.i2c)
        self.ads.gain = 8
        self.chan = AnalogIn(self.ads, ADS.P0)
    
    def value(self):
        value = self.chan.value
        return value
    
    def voltage(self):
        voltage = self.chan.voltage
        return voltage

GP2Y = GP2Y()

iteration = 0
while True:
    os.system('clear')
    
    print(f'buna ziua, iteratia {iteration}')
    print(f'Value: {GP2Y.value()}')
    print(f'Voltage: {GP2Y.voltage()}')
    
    iteration += 1
    time.sleep(1)
