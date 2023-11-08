#!/usr/bin/env python

import rospy
from manager.msg import SteeringControl  # Import the SteeringControl message type

class SteeringNode:
    def __init__(self):
        # Initialize the SteeringNode as a ROS node.
        rospy.init_node("steering_node")

        # Create a subscriber for the "steering control" topic.
        rospy.Subscriber("/steering/steering_control", SteeringControl, self.steering_control_callback)

        # Create a publisher for the "steering control" topic.
        self.steering_control_pub = rospy.Publisher("/manager/steering_control", SteeringControl, queue_size=10)
    ### example
    # Callback function for the "steering control" topic.
    def steering_control_callback(self, msg):
        if msg.enabled:
            # Set a constant desired steering angle (e.g., 0.1 radians)
            desired_steering = 0.1  # You can change this to your desired angle

            # Send the desired steering angle as a command
            self.send_steering_cmd(desired_steering)

            # Log the desired steering angle
            rospy.loginfo("Desired Steering Angle: %.2f", desired_steering)
        else:
            # Steering control is disabled, you might want to set the steering angle to 0
            self.send_steering_cmd(0.0)

    # Function to send steering commands to the manager
    def send_steering_cmd(self, angle):
        msg = SteeringControl()
        msg.enabled = True  # Enable steering control
        msg.angle = angle
        self.steering_control_pub.publish(msg)

if __name__ == "__main__":
    steering_node = SteeringNode()
    rospy.spin()
