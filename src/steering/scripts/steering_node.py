#!/usr/bin/env python

import rospy
from manager.msg import SteeringControl
from std_msgs.msg import Float32

class SteeringNode:
    def __init__(self):
        self.steering_control: bool = False
        # Initialize the DriveNode as a ROS node.
        rospy.init_node("steering_node")

        # Create a subscriber for the "steering/steering_control" topic.
        rospy.Subscriber("/steering/steering_control", SteeringControl, self.steering_control_callback)

        # Create a publisher for the "new_steering" topic.
        self.steer_pub = rospy.Publisher("/manager/steering", Float32, queue_size=10)

    
    # Callback function for the "drive/steering_control" topic.
    def steering_control_callback(self, msg):
        self.enable_steering_control(msg.enabled)
        self.calculate_steering(msg)
    def enable_steering_control(self,  enable: bool):
        self.steering_control = enable

    # Calculate steering on control system
    def calculate_steering(self, msg: SteeringControl):
        if self.steering_control:
            desired_steering = msg.steering_angle
            ### Put calculating codes
            # Maybe using current steeing angle and desired steering..

            # Example
            steer = 0.3  # Change this value as needed
            self.steer_pub.publish(Float32(steer))
            # Log the desired steering
            # rospy.loginfo("Desired Steering Angle: %.2f", desired_steering)
        else: 
            pass


if __name__ == "__main__":
    steering_node = SteeringNode()
    rospy.spin()
