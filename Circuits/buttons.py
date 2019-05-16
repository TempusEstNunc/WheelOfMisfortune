import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(16, GPIO.IN)

#setup for the blue button (Player 1)
def turnOnButton():
    GPIO.output(17, GPIO.HIGH)

def turnOffButton():
    GPIO.output(17, GPIO.LOW)

def ButtonPressed():
    return GPIO.input(16) == 1

def closingTime():
    GPIO.cleanup()
