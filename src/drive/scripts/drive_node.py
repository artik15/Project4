#!/usr/bin/env python

import rospy
from manager.msg import SpeedControl
from std_msgs.msg import Float32

class DriveNode:
    def __init__(self):
        self.control_enabled = False
        # Initialize the DriveNode as a ROS node.
        rospy.init_node("drive_node")

        # Create a subscriber for the "drive/speed_control" topic.
        rospy.Subscriber("/drive/speed_control", SpeedControl, self.speed_control_callback)

        # Create a publisher for the "desired_speed" topic.
        self.desired_speed_pub = rospy.Publisher("/manager/throttle", Float32, queue_size=10)

    # Callback function for the "drive/speed_control" topic.
    def speed_control_callback(self, msg):
        self.control_enabled = msg.enabled
        # Set the received speed command as the desired speed
        self.desired_speed = msg.speed
        # Log the desired speed
        rospy.loginfo("Desired Speed: %.2f", self.desired_speed)

    # Function to perform drive actions based on the desired speed
    def perform_drive_action(self):
        # Implement your custom drive actions here based on the desired speed
        pass

    def run(self):
        loop = rospy.Rate(10.0) # frequency in Hz
        while not rospy.is_shutdown():
            self.perform_drive_action()
            loop.sleep()

if __name__ == "__main__":
    drive_node = DriveNode()
    rospy.spin()
