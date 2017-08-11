import math
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

pin1LED = 8
pin2LED = 10
pin3LED = 12

GPIO.setup(pin1LED,GPIO.OUT)
GPIO.setup(pin2LED,GPIO.OUT)
GPIO.setup(pin3LED,GPIO.OUT)


hz = 4000
pwm1=GPIO.PWM(pin1LED,hz)
pwm2=GPIO.PWM(pin2LED,hz)
pwm3=GPIO.PWM(pin3LED,hz)
pwm1.start(0)
pwm2.start(0)
pwm3.start(0)

GPIO.output(pin1LED,GPIO.HIGH)
GPIO.output(pin2LED,GPIO.HIGH)
GPIO.output(pin3LED,GPIO.HIGH)
time.sleep(1)

while(1):
    amt1 = 100*(1 + math.sin(time.time()*math.pi*2.0*0.19)) / 2
    amt2 = 100*(1 + math.sin(time.time()*math.pi*2.0*0.23)) / 2
    amt3 = 100*(1 + math.sin(time.time()*math.pi*2.0*0.17)) / 2
    pwm1.ChangeDutyCycle(amt1)
    pwm2.ChangeDutyCycle(amt2)
    pwm3.ChangeDutyCycle(amt3)


