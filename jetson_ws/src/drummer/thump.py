#!/usr/bin/python
#import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_Stepper
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

import time, sys
#import atexit
import rospy
from std_msgs.msg import Bool
from beat_msgs.msg import Beat


# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)


#myStepper.setSpeed(30)           # 30 RPM
def thump():
    myStepper.setSpeed(254) # speed  in range (0,255)
    myStepper.step(30, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)
    myStepper.setSpeed(100)
    myStepper.step(30, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)

    # OPTION 2:
    # switch state on callback, count steps on main loop and roll back however many we got in

def main(real):
    # create a default object, no changes to I2C address or frequency
    mh = Adafruit_MotorHAT()
    rospy.on_shutdown(turnOffMotors)
    # atexit.register(turnOffMotors)


    myStepper = mh.getStepper(200, 2) # 200 steps/rev, motor port #1

    if real:
        thump_sub = rospy.Subscriber('/thumps', Bool, thump())
    else:
        #directly from beat detector, mostly for testing
        beat_sub = rospy.Subscriber('/beats', Beat, thump())

    rospy.init_node('beat_player_node', log_level=rospy.INFO, anonymous=True)
    rate = rospy.Rate(100)

    while not rospy.is_shutdown():
        rospy.rate.sleep()




if __name__ == '__main__':
    mode=(sys.argv[1] if len(sys.argv) >1 else 1)

    sys.exit(main(mode))
