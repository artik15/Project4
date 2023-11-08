#!/usr/bin/env python

import rospy
from std_msgs.msg   import String, Float32
from carla_msgs.msg import CarlaEgoVehicleControl, CarlaEgoVehicleStatus
from manager.msg    import SpeedControl, SteeringControl

class ManagerNode:
    def __init__(self) -> None:
        self.control_cmd = CarlaEgoVehicleControl()
        self.speed_control: bool = False
        self.steering_control: bool = False

    def init_communication(self) -> None:
        ### Init all publishers
        self.vehicle_control_pub = rospy.Publisher("/carla/ego_vehicle/vehicle_control_cmd", CarlaEgoVehicleControl, queue_size=10)
        self.speed_control_pub = rospy.Publisher("/drive/speed_control", SpeedControl, queue_size=10)
        self.current_velocity_pub = rospy.Publisher("/drive/current_velocity", Float32, queue_size=10)
        self.steering_control_pub = rospy.Publisher("/steering/steering_control", SteeringControl, queue_size=10)

        ### Init all subscribers
        rospy.Subscriber("/manager/speed_control", SpeedControl, self.speed_control_callback)
        rospy.Subscriber("/carla/ego_vehile/vehicle_status", CarlaEgoVehicleStatus, self.current_velocity_callback)
        rospy.Subscriber("/manager/throttle", Float32, self.received_throttle_callback)
        rospy.Subscriber("/manager/steering_control", SteeringControl, self.steering_control_callback)
        rospy.Subscriber("/manager/steering", Float32, self.received_steering_callback)

        

    ### Subscriber callbacks    

    def current_velocity_callback(self, msg: CarlaEgoVehicleStatus):
        self.current_velocity_pub.publish(Float32(msg.velocity))

    def speed_control_callback(self, msg: SpeedControl):
        self.enable_speed_control(msg.enabled)
        self.send_speed_cmd(msg)

    def received_throttle_callback(self, msg: Float32):
        self.update_throttle(msg.data)

    def steering_control_callback(self, msg: SteeringControl):
        self.enable_steering_control(msg.enabled)
        self.send_steering_cmd(msg)

    def received_steering_callback(self, msg: Float32):
        self.update_steering(msg.data)

    ### Steering control
    def enable_steering_control(self, enable: bool):
        self.steering_control = enable
        if not enable:
            self.update_throttle(0.0)

    def send_steering_cmd(self, msg: SteeringControl):
        if self.steering_control:
            self.steering_control_pub.publish(msg)

    def update_steering(self, new_stearing: float):
        if not self.steering_control:
            return
        
        if new_stearing <= -1.0:
            self.control_cmd.steer = -1.0
        elif new_stearing >= 1.0:
            self.control_cmd.steer = 1.0
        else:
            self.control_cmd.steer = new_stearing
        
    ### Speed/throttle control
    def enable_speed_control(self,  enable: bool):
        self.speed_control = enable

    def send_speed_cmd(self, msg: SpeedControl):
        if self.speed_control:
            self.speed_control_pub.publish(msg)

    def update_throttle(self, new_throttle: float):
        if not self.speed_control:
            return
        
        if new_throttle <= 0.0:
            self.control_cmd.throttle = 0.0
        elif new_throttle >= 1.0:
            self.control_cmd.throttle = 1.0
        else:
            self.control_cmd.throttle = new_throttle

    ### Control command
    def send_control_cmd(self):
        if self.speed_control or self.steering_control:
            self.vehicle_control_pub.publish(self.control_cmd)

    def run(self):
        self.init_communication()
        loop = rospy.Rate(10.0) # frequency in Hz
        while not rospy.is_shutdown():
            self.send_control_cmd()
            loop.sleep()

if __name__ == "__main__":
    rospy.init_node("manager_node")
    manager = ManagerNode()
    manager.run()