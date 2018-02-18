#!/usr/bin/python
#import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_Stepper
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

import time, sys
#import atexit
import rospy
from std_msgs.msg import Bool
from beat_msgs.msg import Beat

class StepperHat(object):
    
    def __init__(self):
         self.mh = Adafruit_MotorHAT()
         self.stepper = self.mh.getStepper(200, 2)
    # recommended for auto-disabling motors on shutdown!
    def turnOffMotors(self):
        self.mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

    def fwd(self, spd):
        self.stepper.setSpeed(spd) # speed  in range (0,255)
        self.stepper.step(30, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)
    def bck(self,spd):
        self.stepper.setSpeed(spd)
        self.stepper.step(30, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)   

#stepper.setSpeed(30)           # 30 RPM
    def thump(self, data):
        
        self.fwd(254)
        self.bck(254)

    # OPTION 2:
    # switch state on callback, count steps on main loop and roll back however many we got in
    def noise(self, data):
        print(rospy.Time.now())

def main(inp,out):
    
    rospy.init_node('beat_player_node', log_level=rospy.INFO, anonymous=True)
    rate = rospy.Rate(100)
    # create a default object, no changes to I2C address or frequency
    if out:
        hat=StepperHat()
        rospy.on_shutdown(hat.turnOffMotors) # atexit.register(turnOffMotors)
        hat.cb= hat.thump
    else: hat.cb = hat.noise
        



    # 200 steps/rev, motor port #1

    if inp:
        thump_sub = rospy.Subscriber('/thumps', Bool, hat.cb)
    else:
        #directly from beat detector, mostly for testing
        beat_sub = rospy.Subscriber('/beats', Beat, hat.cb)


  

    while not rospy.is_shutdown():
        rate.sleep()




if __name__ == '__main__':
    inp=(int(sys.argv[1]) if len(sys.argv) >1 else 1) #which topic  
    out=(int(sys.argv[2]) if len(sys.argv) >2 else 1) #which output 
    
    sys.exit(main(inp, out))s
