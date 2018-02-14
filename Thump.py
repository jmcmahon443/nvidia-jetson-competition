#!/usr/bin/python
#import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_Stepper
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

import time
import atexit

# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT()

# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

myStepper = mh.getStepper(200, 2) # 200 steps/rev, motor port #1
#myStepper.setSpeed(30)           # 30 RPM

while (True):
    print("Thump")
    myStepper.setSpeed(254)
    myStepper.step(18, Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.DOUBLE)
    myStepper.setSpeed(50)
    myStepper.step(18, Adafruit_MotorHAT.FORWARD, Adafruit_MotorHAT.DOUBLE)
