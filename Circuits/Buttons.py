import Rpi.GPIO as GPIO
from time import sleep

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(4, GPIO.IN)

#setup for the blue button (Player 1)
def turnOnBlueButton():
    GPIO.output(19, GPIO.HIGH)

def turnOffBlueButton():
    GPIO.output(19, GPIO.LOW)

def blueButtonPressed():
    return GPIO.input(16) is True

def blueButtonLock():
    turnOffGreenButton()
    turnOffRedButton()

def blueButtonReleased():
    turnOffBlueButton()

#setup for the green button (Player 2)
def turnOnGreenButton():
    GPIO.output(20, GPIO.HIGH)

def turnOffGreenButton():
    GPIO.output(20, GPIO.LOW)

def greenButtonPressed():
    return GPIO.input(13) is True

def greenButtonLock():
    turnOffBlueButton()
    turnOffRedButton()

def greenButtonReleased():
    turnOffGreenButton()

#setup for the yellow button (Player 3)
def turnOnYellowButton():
    GPIO.output(21, GPIO.HIGH)

def turnOffYellowButton():
    GPIO.output(21, GPIO.LOW)

def YellowButtonPressed():
    return GPIO.input(12) is True

def YellowButtonLock():
    turnOffBlueButton()
    turnOffGreenButton()

def YellowButtonReleased():
    turnOffYellowButton()

#setup for the red button (Game Host)
def turnOnRedButton():
    GPIO.output(18, GPIO.HIGH)

def turnOffRedButton():
    GPIO.output(18, GPIO.LOW)

def RedButtonPressed():
    return GPIO.input(17) is True

def RedButtonLock():
    turnOffBlueButton()
    turnOffGreenButton()
    turnOffYellowButton()

def RedButtonReleased():
    turnOffRedButton()

turnOnBlueButton()
turnOnGreenButton()
turnOnYellowButton()

while(True):
    if blueButtonPressed():
        blueButtonLock()
        blueButtonReleased()
    if greenButtonPressed():
        greenButtonLock()
        greenButtonReleased()
    if yellowButtonPressed():
        yellowButtonLock()
        yellowButtonReleased()
    if redButtonPressed():
        turnOnRedButton()
        redButtonLock()
        while(redButtonReleased()):
            sleep(0.5)
        redButtonReleased()
