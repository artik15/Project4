#!/usr/bin/env python

import rospy
from manager.msg import SteeringControl
from steering_controller.controller import ControllerSteering
from std_msgs.msg import Float32

class SteeringNode:
    def __init__(self) -> None:
        self.steering_control: bool = False
        self.desired_steering = SteeringControl()

    def init_communication(self) -> None:
        self.steer_pub = rospy.Publisher("/manager/steering", Float32, queue_size=10)
        rospy.Subscriber("/steering/steering_control", SteeringControl, self.steering_control_callback)

    def steering_control_callback(self, msg):
        self.enable_steering_control(msg.enabled)
        self.desired_steering = msg

    def enable_steering_control(self, enable: bool):
        self.steering_control = enable

    def calculate_steering(self, msg: SteeringControl):
            if self.steering_control:
                
                ### Put calculating codes
                ### Maybe using current steering_angle and desired steering..

                # Example
                steer = msg.steering_angle
                self.steer_pub.publish(steer)

            else: 
                pass

    def send_steering_cmd(self):
        if self.steering_control:
            self.calculate_steering(self.desired_steering)

    def run(self):
        self.init_communication()
        loop = rospy.Rate(10.0)  
        while not rospy.is_shutdown():
            self.send_steering_cmd()
            loop.sleep()

if __name__ == "__main__":
    rospy.init_node("steering_node")
    steering_node = SteeringNode()
    steering_node.run()
