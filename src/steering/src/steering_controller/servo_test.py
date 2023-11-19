import steering_controller.servo_motor as servo_motor
import steering_controller.servo_encoder as servo_encoder
from steering_controller.servo_parameters import *
import time

print(servo_pin)

S1 = servo_motor.ServoMotor
E1 = servo_encoder.ServoEncoder
pwm = S1.configure(S1, servo_pin, pwm_frequency)
bus = E1.defineBus(1)
E1.readFirstAngle(E1,bus)

while True:
    input_angle = float(input())
    S1.change_angle(S1, pwm, input_angle)
    time.sleep(time_sleep_read_angle)
    read_angle = E1.getAngle(E1,bus)
    print("angle = ", read_angle)


