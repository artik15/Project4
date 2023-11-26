#!/usr/bin/env python
import RPi.GPIO as GPIO
from time import sleep
from drive_controller.controller import Controller
from drive_controller.motor import Motor
from drive_controller.encoder import Encoder
from drive_controller.driver_parameters import *
import rospy
from manager.msg import SpeedControl
from std_msgs.msg import Float32

class DriveNode:
    def __init__(self) -> None:
        self.speed_control: bool = False
        self.desired_speed = SpeedControl()
        self.current_velocity = Float32()

    def init_communication(self) -> None:
        self.throttle_pub = rospy.Publisher("/manager/throttle", Float32, queue_size=10)
        rospy.Subscriber("/drive/speed_control", SpeedControl, self.speed_control_callback)
        rospy.Subscriber("/drive/current_velocity", Float32, self.current_velocity_callback)
    ### Subscriber callbacks    

    def speed_control_callback(self, msg: SpeedControl):
        #print("CB")
        self.enable_speed_control(msg.enabled)
        self.desired_speed = msg.speed
        
    def current_velocity_callback(self, msg):
        self.current_velocity = msg
        
    def enable_speed_control(self,  enable: bool):
        self.speed_control = enable

    # Calculate throttle on control system
    def calculate_throttle(self, current_velocity: float) -> float:
        return current_velocity/60.0

    def send_throttle_cmd(self, throttle):
        if self.speed_control:
            self.throttle_pub.publish(Float32(throttle))
            

    def run(self):
        self.init_communication()
        loop = rospy.Rate(10.0) # frequency in Hz
        #### added code
        prev = 0
        next = 0
        e1 = Encoder(dt,clk)
        M1 = Motor(in1,in2,en)
        C1 = Controller(k, t, tp, 0.0)
        C1.parameterize(k, t, tp) 
        #0.9,0.3 /0.92,0.8
        PWM = M1.configure(in1,in2,en,100)
        #M1.change_direction("Forward")
        # M1.change_velocity(M1,PWM, 40)
        ###

        while not rospy.is_shutdown():
            if self.speed_control:
                #print("1")
                next = e1.getValue()
                pv = (60*abs(next - prev))/(110)
                cv = C1.calc_cv(self.desired_speed, pv)
                M1.change_velocity(PWM,cv)
                prev = next
                print(f"cv {cv} pv {pv}")
                throttle = self.calculate_throttle(pv)
                self.send_throttle_cmd(throttle)
            else:
                M1.change_velocity(PWM,0.0)
                prev = 0
                next = 0
            
            loop.sleep()

if __name__ == "__main__":
    rospy.init_node("drive_node")
    drive_node = DriveNode()
    drive_node.run()
