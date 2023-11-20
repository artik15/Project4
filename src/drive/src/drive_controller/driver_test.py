import RPi.GPIO as GPIO
from time import sleep
import controller
import motor
from encoder import Encoder
from driver_parameters import *
t1 = []
y1 = []
next = 0
prev = 0
i = 0
t = 0.1
sp = 30
e1 = Encoder(dt,clk)
M1 = motor.Motor
#C1 = Controller.Controller
#C1.parameterize(C1, k, t, tp)  #0.9,0.3 /0.92,0.8
PWM = M1.configure(M1,in1,in2,en,100)
M1.change_direction(M1,"Backward")
#M1.change_velocity(M1,PWM,40)
M1.change_velocity(M1,PWM,100)
while True:
    #e1.clearValue()
    next = e1.getValue()
    pv = (60*abs(next - prev))/(t*1280)
    y1.append(pv)
    t1.append(t*(i+1))
    print("pv= ",pv)
    prev = next
    #print("t= ",t*(i+1))
    #cv = C1.calc_cv(C1,sp,pv)
    #print("e =",30-pv)
    #M1.change_velocity(M1,PWM,cv)
    #print("u= ",cv)
    #i = i+1
    #if 0.5*(i) > 4:
        #sp = 55
    sleep(t)
M1.stop(M1)
#print(t1)
#print(y1)

