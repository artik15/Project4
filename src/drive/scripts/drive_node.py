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

    def speed_control_callback(self, msg):
        self.enable_speed_control(msg.enabled)
        self.desired_speed = msg
        
    def current_velocity_callback(self, msg):
        self.current_velocity = msg
        
    def enable_speed_control(self,  enable: bool):
        self.speed_control = enable

    # Calculate throttle on control system
    def calculate_throttle(self, msg: SpeedControl , current_velocity: Float32):
        throttle = 0
        
        if self.speed_control:
            
            if msg.speed > current_velocity.data:
                throttle = 1
            elif msg.speed < current_velocity.data:
                throttle = 0
            else:
                pass
            
        else: 
            pass

        self.throttle_pub.publish(throttle)

    def send_throttle_cmd(self):
        if self.speed_control:
            self.calculate_throttle(self.desired_speed, self.current_velocity)
            

    def run(self):
        self.init_communication()
        loop = rospy.Rate(10.0) # frequency in Hz

        #### added code
        e1 = Encoder(dt,clk)
        M1 = Motor()
        C1 = Controller()
        C1.parameterize(C1, k, t, tp)  #0.9,0.3 /0.92,0.8
        PWM = M1.configure(M1,in1,in2,en,100)
        # M1.change_direction(M1,"Forward")
        # M1.change_velocity(M1,PWM, 40)
        ###


        while not rospy.is_shutdown():
            self.send_throttle_cmd()
            loop.sleep()

if __name__ == "__main__":
    rospy.init_node("drive_node")
    drive_node = DriveNode()
    drive_node.run()
