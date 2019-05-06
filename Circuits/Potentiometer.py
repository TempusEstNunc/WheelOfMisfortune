import RPi.GPIO as GPIO
import board
import busio
import adafruit_ads1x15.ads1015 as ADS
import adafruit_ads1x15.analog_in import AnalogIn

i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1015(i2c)
chan = AnalogIn(ads, ADS.P0)
print(chan.value, chan.voltage)

#use resistor to lower volatage to 3V or less
#cannot incorporate GPIO values until sautering is finished
