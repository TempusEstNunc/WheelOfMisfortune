#imports sleep from time
from time import sleep
#imports the adafruit library for the potentiometer and the analog-to-digital adapter
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1015()
#gain controls voltage range
#2/3 = +/-6.144V
#1 = +/-4.096V
#2 = +/-2.048V
#4 = +/-1.024V
#8 = +/-0.512V
#16 = +/-0.256V
GAIN = 1

while True:
    #reads all the ADC channel values in a list
    values = [0]*4
    for i in range(4):
        #reads the specified ADC channel using the previously set gain value
        values[i] = adc.read_adc(i, gain=GAIN)
        #each value is a 12 bit signed integer value
    #prints the ADC values
    print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
    #pauses for half a second
    sleep(0.1)
