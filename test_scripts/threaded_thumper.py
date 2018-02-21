from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor
import time
import atexit
import threading
import random


# create a default object, no changes to I2C address or frequency
mh = Adafruit_MotorHAT()

# create empty threads (these will hold the stepper 1 and 2 threads)
st1 = threading.Thread()


# recommended for auto-disabling motors on shutdown!
def turnOffMotors():
    mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
    mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)

atexit.register(turnOffMotors)

myStepper1 = mh.getStepper(200, 1)      # 200 steps/rev, 1.8 deg/step motor port #1

spd=300
        # 30 RPM



stepstyles = [Adafruit_MotorHAT.SINGLE, Adafruit_MotorHAT.DOUBLE, Adafruit_MotorHAT.INTERLEAVE, Adafruit_MotorHAT.MICROSTEP] # https://en.wikipedia.org/wiki/Stepper_motor#Phase_urent_waveforms

def stepper_worker(stepper, numsteps, direction, style):
    #print("Steppin!")
    stepper.step(numsteps, direction, style)
    #print("Done")

dir_toggle=0
while (True):
    myStepper1.setSpeed(spd)
    print("speed", spd)
    if not st1.isAlive():
        dir_toggle ^=1
        print("Stepper 1"),
        if ( dir_toggle ):
            dir = Adafruit_MotorHAT.BACKWARD
            print("backward")


        steps=(10)
        print("%d steps" % steps)
        st1 = threading.Thread(target=stepper_worker, args=(myStepper1, steps, dir, Adafruit_MotorHAT.DOUBLE))
        st1.start()
        spd+=10


    time.sleep(0.1)
