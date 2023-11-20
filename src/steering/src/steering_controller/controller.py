from steering_controller.servo_parameters import *

class ControllerSteering:
    k = 0.0     # Gain
    Ti = 0.0    # Integral Constant
    Tp = 0.0    # Sampling period
    integral_sum = 0.0 # Sum for integral element
    supp_value = 0.0

    def __init__(self,K,Ti,Tp, IntegralSum, SuppValue) -> None:
        self.k = K
        self.Ti = Ti
        self.Tp = Tp
        self.integral_sum = IntegralSum
        self.supp_value = SuppValue


    # Parameterization Function
    def parameterize(self, ext_k, ext_Ti, ext_Tp, ext_supp_value):
        self.k = ext_k
        self.Ti = ext_Ti
        self.Tp = ext_Tp
        self.integral_sum = 0.0
        self.supp_value = ext_supp_value
        return 0
    
    # Get Set Point Value function
    def get_sp(self,):
        
        #For future development

        return 0
    
    # Get Actual Value function
    def get_pv(self,):

        #For future development

        return 0 
        
    # Function for calculating actual control value
    def calc_cv(self,sp_value, p_value,):
        error_k = sp_value - p_value
        self.integral_sum = self.integral_sum + error_k
        cv = self.k * (error_k + (self.Tp/self.Ti)*(self.integral_sum)) + self.supp_value
        
        ## limiting the control value and Anti-windup mechanism
        if cv >= right_angle_limit:
            cv = right_angle_limit
            self.integral_sum = self.integral_sum - error_k
        if cv <= left_angle_limit:
            cv = left_angle_limit
            self.integral_sum = self.integral_sum - error_k

        return cv
