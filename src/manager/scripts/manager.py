#!/usr/bin/env python

import rospy
from std_msgs.msg import String

class ManagerNode:
    def __init__(self) -> None:
        # init all necessary variables
        pass

    def init_communication(self) -> None:
        # Init all publishers

        # Init all subscribers
        rospy.Subscriber("/test_topic", String, self.sample_callback)
        
    def sample_callback(self, msg):
        print(msg)

    def run(self):
        self.init_communication()
        loop = rospy.Rate(10.0) # frequency in Hz
        while not rospy.is_shutdown():
            loop.sleep()

if __name__ == "__main__":
    rospy.init_node("manager")
    manager = ManagerNode()
    manager.run()