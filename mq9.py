import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

class MQ:
	def __init__(self, i2c):
		self.ads = ADS.ADS1115(i2c, address=0x48)
		self.ads.gain = 8
		self.channel = AnalogIn(self.ads, ADS.P0)
	
	def value(self):
		value = self.chanel.value
		return value

	def voltage(self):
		voltage = self.chanel.voltage
		return voltage
