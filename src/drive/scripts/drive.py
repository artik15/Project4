#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
from manager.msg import SpeedControl

class DriveNode:
    def __init__(self):
        # Initialize the DriveNode as a ROS node.
        rospy.init_node("drive_node")

        # Create a subscriber for the "speed control" topic.
        rospy.Subscriber("/drive/speed_control", SpeedControl, self.speed_control_callback)

        # Create a publisher for the "/manager/speed_control" topic.
        self.manager_speed_control_pub = rospy.Publisher("/manager/speed_control", SpeedControl, queue_size=10)
    ### example
    # Callback function for the "speed control" topic.
    def speed_control_callback(self, msg):
        if msg.enabled:
            # Set a constant desired speed (e.g., 5.0 m/s)
            desired_speed = 5.0  # You can change this to your desired speed

            # Send the desired speed as a command to the manager
            self.send_manager_speed_cmd(desired_speed)

            # Log the desired speed
            rospy.loginfo("Desired Speed: %.2f", desired_speed)
        else:
            pass

    # Function to send speed commands to the manager
    def send_manager_speed_cmd(self, speed):
        msg = SpeedControl()
        msg.enabled = True  # Enable speed control
        msg.speed = speed
        self.manager_speed_control_pub.publish(msg)

if __name__ == "__main__":
    drive_node = DriveNode()
    rospy.spin()