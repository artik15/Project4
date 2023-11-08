#!/usr/bin/env python

import rospy
from manager.msg import SteeringControl
from std_msgs.msg import Float32

class SteeringNode:
    def __init__(self):
        self.control_enabled = False
        # Initialize the SteeringNode as a ROS node.
        rospy.init_node("steering_node")

        # Create a subscriber for the "steering/speed_control" topic.
        rospy.Subscriber("/steering/steering_control", SteeringControl, self.steering_speed_control_callback)

        # Create a publisher for the "desired_steering" topic.
        self.desired_steering_pub = rospy.Publisher("/manager/steering", Float32, queue_size=10)

    # Callback function for the "steering/speed_control" topic.
    def steering_speed_control_callback(self, msg):
        self.control_enabled = msg.enabled
        # Set the received steering angle command as the desired steering angle
        desired_steering = msg.steering_angle

        # Log the desired steering angle
        rospy.loginfo("Desired Steering Angle: %.2f", desired_steering)

    # Function to perform steering actions based on the desired steering angle
    def perform_steering_action(self):
        # Implement your custom steering actions here based on the desired steering angle
        pass

    def run(self):
        loop = rospy.Rate(10.0) # frequency in Hz
        while not rospy.is_shutdown():
            self.perform_steering_action()
            loop.sleep()

if __name__ == "__main__":
    steering_node = SteeringNode()
    steering_node.run()
