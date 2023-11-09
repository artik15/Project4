#!/usr/bin/env python

import rospy
from manager.msg import SpeedControl
from std_msgs.msg import Float32

class DriveNode:
    def __init__(self):
        self.speed_control: bool = False
        # Initialize the DriveNode as a ROS node.
        rospy.init_node("drive_node")

        # Create a subscriber for the "drive/speed_control" topic.
        rospy.Subscriber("/drive/speed_control", SpeedControl, self.speed_control_callback)

        # Create a publisher for the "throttle" topic.
        self.throttle_pub = rospy.Publisher("/manager/throttle", Float32, queue_size=10)

    
    # Callback function for the "drive/speed_control" topic.
    def speed_control_callback(self, msg):
        self.enable_speed_control(msg.enabled)
        self.calculate_throttle(msg)
    def enable_speed_control(self,  enable: bool):
        self.speed_control = enable

    # Calculate throttle on control system
    def calculate_throttle(self, msg: SpeedControl):
        if self.speed_control:
            desired_speed = msg.speed
            ### Put calculating codes
            
            # Maybe using current speed and desired speed..

            # Example
            throttle = 0.7
            self.throttle_pub.publish(throttle)
            # test - Log the desired speed
            # rospy.loginfo("Desired Speed: %.2f", desired_speed)
        else: 
            pass


if __name__ == "__main__":
    drive_node = DriveNode()
    rospy.spin()
