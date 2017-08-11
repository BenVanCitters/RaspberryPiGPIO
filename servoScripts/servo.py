import RPi.GPIO as GPIO
import time

class MotorController:
    pin_num = 12
    base_hertz = 50
    duty_cycle_start = 2.5
    duty_cycle_end = 12.5

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin_num, GPIO.OUT)
        self.pwm = GPIO.PWM(self.pin_num, self.base_hertz)
        self.pwm.start(self.duty_cycle_start)

    def move_motor(self, range_pct=0):
        rng = self.duty_cycle_end - self.duty_cycle_start
        dc = self.duty_cycle_start + range_pct*rng
        print(str(dc))
        self.pwm.ChangeDutyCycle(dc)

    def lerpMotor(self, from_range_pct, to_range_pct, time_length):
        rng = self.duty_cycle_end - self.duty_cycle_start
        increments = 100

        wait_duration = time_length *1.0/ increments
        start_dc = self.duty_cycle_start + rng * from_range_pct
        end_dc = self.duty_cycle_start + rng * to_range_pct
        start_end_range = end_dc-start_dc

        print( "wait_duration: " + str(wait_duration))
        for i in range(0,increments,1):
            pct_through = i*1.0/increments
            target_dc = start_dc + start_end_range * pct_through
            #print(str(target_dc))
            self.pwm.ChangeDutyCycle(target_dc)
            time.sleep(wait_duration)


motorC = MotorController()

up_percent = .5
down_percent = 0.0

print('moving servo to .5')
motorC.lerpMotor( down_percent, up_percent, time_length=1)
