#!/usr/bin/env python

import rospy
from manager.msg import SpeedControl
from std_msgs.msg import Float32

class DriveNode:
    def __init__(self) -> None:
        self.speed_control: bool = False
        self.desired_speed = SpeedControl()

    def init_communication(self) -> None:
        self.throttle_pub = rospy.Publisher("/manager/throttle", Float32, queue_size=10)
        rospy.Subscriber("/drive/speed_control", SpeedControl, self.speed_control_callback)

    ### Subscriber callbacks    

    def speed_control_callback(self, msg):
        self.enable_speed_control(msg.enabled)
        self.desired_speed = msg
        
    def enable_speed_control(self,  enable: bool):
        self.speed_control = enable

    # Calculate throttle on control system
    def calculate_throttle(self, msg: SpeedControl):
        if self.speed_control:
            
            ### Put calculating codes
            ### Maybe using current speed and desired speed..

            # Example
            throttle = msg.speed
            self.throttle_pub.publish(throttle)
            # test - Log the desired speed
            # rospy.loginfo("Desired Speed: %.2f", desired_speed)
        else: 
            pass
    def send_throttle_cmd(self):
        if self.speed_control:
            self.calculate_throttle(self.desired_speed)
            

    def run(self):
        self.init_communication()
        loop = rospy.Rate(10.0) # frequency in Hz
        while not rospy.is_shutdown():
            self.send_throttle_cmd()
            loop.sleep()

if __name__ == "__main__":
    rospy.init_node("drive_node")
    drive_node = DriveNode()
    drive_node.run()
