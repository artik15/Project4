#!/usr/bin/env python

import rospy
from manager.msg import SteeringControl
from std_msgs.msg import Float32

class SteeringNode:
    def __init__(self):
        # Initialize the SteeringNode as a ROS node.
        rospy.init_node("steering_node")

        # Create a subscriber for the "steering/speed_control" topic.
        rospy.Subscriber("/steering/speed_control", SteeringControl, self.steering_speed_control_callback)

        # Create a publisher for the "desired_steering" topic.
        self.desired_steering_pub = rospy.Publisher("/steering/desired_steering", Float32, queue_size=10)

    # Callback function for the "steering/speed_control" topic.
    def steering_speed_control_callback(self, msg):
        if msg.enabled:
            # Set the received steering angle command as the desired steering angle
            desired_steering = msg.steering_angle

            # Publish the desired steering angle
            self.desired_steering_pub.publish(Float32(desired_steering))

            # Perform other actions based on the desired steering angle
            self.perform_steering_action(desired_steering)

            # Log the desired steering angle
            rospy.loginfo("Desired Steering Angle: %.2f", desired_steering)
        else:
            pass

    # Function to perform steering actions based on the desired steering angle
    def perform_steering_action(self, desired_steering):
        # Implement your custom steering actions here based on the desired steering angle
        pass

if __name__ == "__main__":
    steering_node = SteeringNode()
    rospy.spin()
