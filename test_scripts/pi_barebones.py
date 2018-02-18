#!/usr/bin/python
#import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_Stepper
import sys, atexit, time
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)


#myStepper.setSpeed(30)           # 30 RPM
def thump():
    myStepper.setSpeed(254) # speed  in range (0,255)
    myStepper.step(100, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)
    time.sleep(2)
    myStepper.setSpeed(250)
    myStepper.step(100, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)




if __name__ == '__main__':
    # create a default object, no changes to I2C address or frequency
    mh = Adafruit_MotorHAT()
    atexit.register(turnOffMotors) # rospy.on_shutdown(turnOffMotors)

    myStepper = mh.getStepper(200, int(sys.argv[1]))

    while (1):
        key = raw_input()
        thump()
