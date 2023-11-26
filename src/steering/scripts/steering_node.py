#!/usr/bin/env python

import rospy
from manager.msg import SteeringControl
import steering_controller.servo_motor as ServoMotor
from steering_controller.controller import ControllerSteering
from steering_controller.servo_parameters import *
from std_msgs.msg import Float32

class SteeringNode:
    def __init__(self) -> None:
        self.steering_control: bool = False
        self.current_steer = 0
        self.desired_steering = SteeringControl()

    def init_communication(self) -> None:
        # self.steer_pub = rospy.Publisher("/manager/steering", Float32, queue_size=10)
        rospy.Subscriber("/steering/steering_control", SteeringControl, self.steering_control_callback)
        rospy.Subscriber("/steering/current_steer", Float32, self.current_steer_callback)

        
    def steering_control_callback(self, msg):
        print(msg)
        self.enable_steering_control(msg.enabled)

    def current_steer_callback(self, msg):
        self.current_steer = msg.data

    def enable_steering_control(self, enable: bool):
        self.steering_control = enable

    def calculate_steering(self, current_steer: Float32):
        if self.steering_control:
            steer = 2.1*current_steer + 7    
        else: 
            steer = 7
        #print(steer)
        return steer

    # def send_steering_cmd(self):
    #     if self.steering_control:
    #         self.calculate_steering(self.desired_steering)

    def run(self):
        self.init_communication()
        loop = rospy.Rate(10.0)
        S1 = ServoMotor.ServoMotor()
        pwm = S1.configure(servo_pin, pwm_frequency)
        while not rospy.is_shutdown():
            steer = self.calculate_steering(self.current_steer)
            S1.change_angle(pwm, steer)
            loop.sleep()

if __name__ == "__main__":
    rospy.init_node("steering_node")
    steering_node = SteeringNode()
    steering_node.run()