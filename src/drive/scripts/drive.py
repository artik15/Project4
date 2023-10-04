import rospy
from std_msgs.msg import String, Int32


class drive_Node:
    def __init__(self):
        print('Hello package')
        rospy.Subscriber("/test_topic", Int32, self.msg_callback, queue_size=10)
        self.pub_msg = rospy.Publisher("/test_topic", String, queue_size=10)
        rospy.Timer(rospy.Duration(0.1), self.timer_callback)
        
    def timer_callback(self, event):
        msg = String()
        msg.data = 'Hello'
        self.pub_msg.publish(msg)
    
    def msg_callback(self, msg):
        num = int(msg.data)
        rospy.loginfo('new message! %d', num)
    
    def main(self):
        rospy.spin()

if __name__ == '__main__':
    rospy.init_node('drive_node')
    node = drive_Node()
    node.main()