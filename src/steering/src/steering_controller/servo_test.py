import steering_controller.servo_motor as servo_motor
import steering_controller.servo_encoder as servo_encoder
import steering_controller.controller as servo_controller
from steering_controller.servo_parameters import *
import time

print(servo_pin)
i = 0
t = tp
S1 = servo_motor.ServoMotor
E1 = servo_encoder.ServoEncoder
C1 = servo_controller.ControllerSteering
pwm = S1.configure(S1, servo_pin, pwm_frequency)
C1.parameterize(C1, k, t, tp)
bus = E1.defineBus(1)
E1.readFirstAngle(E1,bus)
sp = - 30

while i*t < 10:
    pv = E1.getAngle(E1, bus)
    print("pv= ", pv)
    print("e= ", sp-pv)
    cv = C1.calc_cv(C1, sp, pv)
    print("u= ", cv)
    S1.change_angle(S1, pwm, cv)
    i = i+1


