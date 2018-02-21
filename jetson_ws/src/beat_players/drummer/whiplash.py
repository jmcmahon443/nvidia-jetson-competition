#! /usr/bin/python
#import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_Stepper
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor, Adafruit_StepperMotor

import time, sys
#import atexit
import rospy
from std_msgs.msg import Bool
from beat_msgs.msg import Beat

revstep=200

class StepperHat(object):
    DIRS=[Adafruit_MotorHAT.BACKWARD, Adafruit_MotorHAT.FORWARD] #backwards is towrad the drum
    HIT_ZONE = -8  # where drum is
    TAP_LINE = 0  # rreturn here if you hve more beats to hit
    RETREAT = 6 # as far back as we go
    HIT_SPEED = 180
    RETREAT_SPEED = 100



    def __init__(self):
         self.mh = Adafruit_MotorHAT()
         self.stepper = self.mh.getStepper(revstep, 1)
         #self.dir_sel = 0 #driection select
         self.dir_sel=1
         self.coming_beats = 0
         self.position = -8 #net count of taken steps

    # recommended for auto-disabling motors on shutdown!
    def turnOffMotors(self):
        self.mh.getMotor(1).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(2).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(3).run(Adafruit_MotorHAT.RELEASE)
        self.mh.getMotor(4).run(Adafruit_MotorHAT.RELEASE)


#stepper's callback
    def thump(self, data):
        if self.position > StepperHat.TAP_LINE:
            self.stepper.setSpeed(StepperHat.HIT_SPEED)
            self.dir_sel=0
        self.coming_beats += 1

    def run_stepper(self):

        if (self.position >= StepperHat.RETREAT and not self.coming_beats):
            # or (not self.coming_beats and self.position >= StepperHat.TAP_LINE)

            return False
        else:
            if self.position >= StepperHat.RETREAT:
                self.stepper.setSpeed(StepperHat.HIT_SPEED)
                self.dir_sel=0

            elif self.position < StepperHat.HIT_ZONE:
                self.stepper.setSpeed(StepperHat.RETREAT_SPEED)
                self.dir_sel=1
                self.coming_beats -= 1

            elif self.position >= StepperHat.TAP_LINE and self.coming_beats:  # and self.coming_beats>0: #already checking that

                self.stepper.setSpeed(StepperHat.HIT_SPEED)
                self.dir_sel=0

            self.stepper.oneStep( StepperHat.DIRS[self.dir_sel], Adafruit_MotorHAT.DOUBLE)
            self.position+=(1 if self.dir_sel else -1)

            print(self.position, self.dir_sel, self.coming_beats)
            return self.dir_sel


    # OPTION 2:
    # switch state on callback, count steps on main loop and roll back however many we got in
def noise( data):
    print(rospy.Time.now())

def run_print():
    return False

def main():

    #name=rospy.get_param('name', 'drummer')


    lvl=rospy.get_param('log_level', rospy.INFO)
    rospy.init_node("drummer" , log_level=lvl, anonymous=True)
    out=rospy.get_param('~out')

    fwd_rate = rospy.Rate(StepperHat.HIT_SPEED*revstep/60)
    bck_rate = rospy.Rate(StepperHat.RETREAT_SPEED*revstep/60)

    # create a default object, no changes to I2C address or frequency
    if out:
        hat=StepperHat()
        rospy.on_shutdown(hat.turnOffMotors) # atexit.register(turnOffMotors)
        cb= hat.thump
        run=hat.run_stepper

    else:
        cb = noise
        run=run_print

    hit_sub = rospy.Subscriber("in", Bool, cb)

    # 200 steps/rev, motor port #1
    while not rospy.is_shutdown():
        if run():  bck_rate.sleep()
        else: fwd_rate.sleep()


    # speed  in range (0,255)



if __name__ == '__main__':

    # inp=(int(sys.argv[1]) if len(sys.argv) >1 else rospy.get_param('~in', '/thumps')) #which topic
    # out=(int(sys.argv[2]) if len(sys.argv) >2 else rospy.get_param('~out', True)) #which output

    #inp=rospy.get_param('~in', '/thumps')
    #rospy.loginfo("")
    sys.exit(main())
