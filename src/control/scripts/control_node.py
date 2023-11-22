#!/usr/bin/env python

import rospy
import sys, select, termios, tty
from std_msgs.msg import String, Float32
from manager.msg import SpeedControl, SteeringControl  # Import the new message types

ROSCAR_MAX_ACCELL_VEL = 20
ROSCAR_MAX_STEERING_VEL = 50

ROSCAR_MIN_ACCELL_VEL = -20
ROSCAR_MIN_STEERING_VEL = -50

def getKey():
    # Define and store the initial terminal settings
    initial_settings = termios.tcgetattr(sys.stdin)
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    # Restore the initial terminal settings
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, initial_settings)
    return key

def control_node():
    rospy.init_node('control_node')

    # Create publishers for speed control and steering control
    speed_control_pub = rospy.Publisher('/manager/speed_control', SpeedControl, queue_size=10)
    steering_control_pub = rospy.Publisher('/manager/steering_control', SteeringControl, queue_size=10)

    # Initialize the settings variable
    settings = termios.tcgetattr(sys.stdin)

    linear_vel = 0
    angular_vel = 0

    while not rospy.is_shutdown():
        key = getKey()

        # Process key presses and generate speed and steering control messages
        if key == 'w':
            # Increase linear velocity
            linear_vel += 1
        elif key == 's':
            # Decrease linear velocity
            linear_vel -= 1
        elif key == 'a':
            # Increase angular velocity
            angular_vel -= 1
        elif key == 'd':
            # Decrease angular velocity
            angular_vel += 1
        elif key == ' ' or key == 'x':
            # Stop the vehicle
            linear_vel = 0
            angular_vel = 0
        elif key == '\x03':
            # Ctrl-C to exit
            break

        # Make sure linear and angular velocity are within limits
        linear_vel = max(min(linear_vel, ROSCAR_MAX_ACCELL_VEL), ROSCAR_MIN_ACCELL_VEL)
        angular_vel = max(min(angular_vel, ROSCAR_MAX_STEERING_VEL), ROSCAR_MIN_STEERING_VEL)

        # Create and publish speed control message
        speed_msg = SpeedControl()
        speed_msg.enabled = True  # Enable speed control
        speed_msg.speed = linear_vel
        speed_control_pub.publish(speed_msg)

        # Create and publish steering control message
        steering_msg = SteeringControl()
        steering_msg.enabled = True  # Enable steering control
        steering_msg.steering_angle = angular_vel  # Set the steering angle as per your input
        steering_control_pub.publish(steering_msg)

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

if __name__ == '__main__':
    try:
        control_node()
    except rospy.ROSInterruptException:
        pass
