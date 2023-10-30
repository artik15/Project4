#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32
from manager.msg import SpeedControl

class DriveNode:
    def __init__(self):
        # Initialize the DriveNode as a ROS node.
        rospy.init_node("drive_node")

        # Create a subscriber for the "speed control" topic.
        rospy.Subscriber("/drive/speed_control", SpeedControl, self.speed_control_callback)

    # Callback function for the "speed control" topic.
    def speed_control_callback(self, msg):
        if msg.enabled:
            # Set a constant desired speed (e.g., 5 m/s)
            desired_speed = 5.0  # You can change this to your desired speed

            # Log the desired speed
            rospy.loginfo("Desired Speed: %.2f", desired_speed)
        else:
            # Speed control is disabled, you might want to stop the robot
            pass  # You can add your logic here for stopping the robot

if __name__ == "__main__":
    drive_node = DriveNode()
    rospy.spin()
