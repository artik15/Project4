#!/usr/bin/env python
import rospy

class Motor_Controller:
    k = 0.0     # Gain
    Ti = 0.0    # Integral Constant
    Tp = 0.0    # Sampling period
    integral_sum = 0.0 # Sum for integral element

    sp = 0.0    # Setpoint
    pv = 0.0    # Process value

    def __init__(self,K,Ti,Tp, IntegralSum) -> None:
        self.k = K
        self.Ti = Ti
        self.Tp = Tp
        self.integral_sum = IntegralSum

    def init_communication(self) -> None:

        #For future development

        pass


    # Parameterization Function
    def parameterize(self, ext_k, ext_Ti, ext_Tp, ext_integralSum) -> None:
        self.k = ext_k
        self.Ti = ext_Ti
        self.Tp = ext_Tp
        self.integral_sum = ext_integralSum
    
    
    # Get Set Point Value function
    def get_sp():
        
        #For future development

        return 0
    
    
    # Get Actual Value function
    def get_pv():
        
        #For future development

        return 0 
        
    # Function for calculating actual control value
    def calc_cv(self):
        error_k = self.sp - self.pv
        cv = self.k * (error_k + (self.Tp/self.Ti)*(self.integral_sum + error_k))
        
        ## limiting the control value

        ## Anti-windup mechanism
        
        return cv
    
    #Future development
    def run(self):
        self.init_communication()
        loop = rospy.Rate(10.0) # frequency in Hz, later we can change when we test how it works
        while not rospy.is_shutdown():
            loop.sleep()

if __name__ == "__main__":
    rospy.init_node("drive")
    drive = Motor_Controller()
    drive.run()