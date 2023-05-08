import board
import busio
from adafruit_bme280 import basic as adafruit_bme280

class BME:
    def __init__(self, decimal):
        self.decimal = decimal
        i2c = busio.I2C(board.SCL, board.SDA)

        self.i2c = i2c
        self.bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
        
    def set_decimal(self, decimal):
        self.decimal = decimal
    
    def temp(self, decimal = None):
        if decimal is None:
            decimal = self.decimal
        
        temp = round(self.bme280.temperature, decimal)
        return temp
    
    def pres(self, decimal = None):
        if decimal is None:
            decimal = self.decimal
        
        pres = round(self.bme280.pressure, decimal)
        return pres
    
    def alt(self, decimal = None):
        if decimal is None:
            decimal = self.decimal
        
        alt = round(self.bme280.altitude, decimal)
        return alt
        
    def hum(self, decimal = None):
        if decimal is None:
            decimal = self.decimal
        
        hum = round(self.bme280.relative_humidity, decimal)
        return hum

