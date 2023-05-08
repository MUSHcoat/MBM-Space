import time
import os
import datetime as dt
import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from lora import transmitPackets

from bme280 import BME
from mq9 import MQ
from gp2y import GP2Y


#general defintions
i2c = busio.I2C(board.SCL, board.SDA)
        
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
        print(f"{now.strftime('%d/%m, %H:%M:%S')};{get_current_time()};{BMP.press(4)},{BMP.alt(4)};{HDC.temp(4)},{HDC.hum(4)};{NEO_la},{NEO_lo};{MPU.accel()};{MPU.gyros()};{MPU.magnet()}")        
        
        now = dt.datetime.now()
        payload = f"{now.strftime('%d/%m, %H:%M:%S')};{get_current_time()};{BMP.press(4)},{BMP.alt(4)};{HDC.temp(4)},{HDC.hum(4)};{NEO_la},{NEO_lo};{MPU.accel()};{MPU.gyros()};{MPU.magnet()}"

        transmitPackets(payload)
        print("[ OK ] Payload sent ...")
        
        time.sleep(1)
