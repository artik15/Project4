import smbus
import RPi.GPIO as GPIO
from Serwo_Parametrs import *
from biny import *
class SerwoEncoder:
    def __init__(self) -> None:
        self.first_angle = 0.0
    def readFirstAngle(self, bus):
        self.first_angle = raw_angle(bus.read_i2c_block_data(device_address, re>
    def defineBus(file):
        bus = smbus.SMBus(file)
        return bus
    def getAngle(self,bus):
        angle = raw_angle(bus.read_i2c_block_data(device_address, read_register>
        calculated_angle = angle - self.first_angle
        return calculated_angle





