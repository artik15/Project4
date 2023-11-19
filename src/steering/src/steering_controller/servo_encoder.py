import smbus2 as smbus
import RPi.GPIO as GPIO
from steering_controller.servo_parameters import *
from steering_controller.bins import *

class ServoEncoder:

    def __init__(self) -> None:
        self.first_angle = 0.0

    def readFirstAngle(self, bus):
        self.first_angle = raw_angle(bus.read_i2c_block_data(device_address, read_register_angle))

    def defineBus(file):
        bus = smbus.SMBus(file)
        return bus
    
    def getAngle(self,bus):
        angle = raw_angle(bus.read_i2c_block_data(device_address, read_register_angle))
        calculated_angle = angle - self.first_angle
        return calculated_angle





