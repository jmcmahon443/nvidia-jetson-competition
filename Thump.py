#!/usr/bin/python
#import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_Stepper
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

import time, sys
import atexit
import rospy

from beat_msgs.msg import Beat


# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)


#myStepper.setSpeed(30)           # 30 RPM
def thump():
    myStepper.setSpeed(254) # speed  e (0,255)
    myStepper.step(30, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)
    myStepper.setSpeed(100)
    myStepper.step(30, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)


def main():
    # create a default object, no changes to I2C address or frequency
    mh = Adafruit_MotorHAT()
    atexit.register(turnOffMotors) # rospy.on_shutdown(turnOffMotors)

    myStepper = mh.getStepper(200, 2) # 200 steps/rev, motor port #1
    self.thump_sub = rospy.Subscriber('/predictions', Beat, thump())

    rospy.init_node('beat_player_node', anonymous=True)
    rate = rospy.Rate(100)

    while not rospy.is_shutdown():
        rospy.rate.sleep()
    #myStepper.setSpeed(6000)
    #myStepper.step(50, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.SINGLE)
    #myStepper.setSpeed(100)
    #myStepper.step(50, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.SINGLE)

    #myStepper.setSpeed(3000)
    #myStepper.step(50, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.INTERLEAVE)
    #myStepper.setSpeed(100)
    #myStepper.step(50, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.INTERLEAVE)

    #print("Sleep 0.2 seconnds")
    #time.sleep(0.2)



if __name__ == '__main__':
    sys.exit(main())
