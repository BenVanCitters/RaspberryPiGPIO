import RPi.GPIO as GPIO
import time

class GPIOLEDLight:

    lightOn = False
    pinNum = 10

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.pinNum,GPIO.OUT)

    def switch_light_on(self, switch_on):
        self.lightOn = switch_on
        if switch_on == False:
            GPIO.output(self.pinNum,GPIO.LOW)
        else:
            GPIO.output(self.pinNum,GPIO.HIGH)

light = GPIOLEDLight()
light.switch_light_on(True)
time.sleep(1)
light.switch_light_on(False)

