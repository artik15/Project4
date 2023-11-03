#!/usr/bin/env python

import rospy
from manager.msg import SpeedControl
from std_msgs.msg import Float32

class DriveNode:
    def __init__(self):
        # Initialize the DriveNode as a ROS node.
        rospy.init_node("drive_node")

        # Create a subscriber for the "drive/speed_control" topic.
        rospy.Subscriber("/drive/speed_control", SpeedControl, self.speed_control_callback)

        # Create a publisher for the "desired_speed" topic.
        self.desired_speed_pub = rospy.Publisher("/drive/desired_speed", Float32, queue_size=10)

    # Callback function for the "drive/speed_control" topic.
    def speed_control_callback(self, msg):
        if msg.enabled:
            # Set the received speed command as the desired speed
            desired_speed = msg.speed

            # Publish the desired speed
            self.desired_speed_pub.publish(Float32(desired_speed))

            # Perform other actions based on the desired speed
            self.perform_drive_action(desired_speed)

            # Log the desired speed
            rospy.loginfo("Desired Speed: %.2f", desired_speed)
        else:
            pass

    # Function to perform drive actions based on the desired speed
    def perform_drive_action(self, desired_speed):
        # Implement your custom drive actions here based on the desired speed
        pass

if __name__ == "__main__":
    drive_node = DriveNode()
    rospy.spin()
