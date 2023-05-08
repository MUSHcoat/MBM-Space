import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

class GP2Y:
	def __init__(self, i2c):
		self.ads = ADS.ADS1115(i2c, address=0x48)
		self.channel = AnalogIn(self.ads, ADS.P0)
		
	def read(self):
		vo_measured = self.channel.voltage
		voltage = vo_measured * 5.0 / 32768.0
		dust_density = ((vo_measured / 0.9) - 1.0) * 50.0
		return dust_density
