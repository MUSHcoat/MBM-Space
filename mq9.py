import os
import time

import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

class MQ:
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
