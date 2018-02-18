#!/usr/bin/env python

import csv, sys, time
import rospy
#import pygame #, ppygame.midi as midi
#from playsound import playsound
from std_msgs.msg import Bool
from beat_msgs.msg import Beat

from rhythm import Models


class Player(object):
    KICK='res/kick.mp3'
    NODE_RATE=100
    LIVE=1
    OFF=0

    def __init__(self,mode, predictive, lvl):
        #pygame.init()
        #self.s = pygame.mixer.Sound(Player.kick)

        rospy.init_node('beat_player_node', log_level=lvl, anonymous=True)
        self.lag_adjustment=0.1 #for HW compensation
        self.ahead=2

        if predictive:
            #offset with cur. time
            self.model=Models.RunningAvgFit(rospy.Time.now().to_sec(), 20)
            self.run=self.run_predicted
            self.cb=self.model_cb
        else:
            self.run=self.run_observed
            self.cb=self.beat_cb
            self.beats=[0]
         #add the actuator delay here, subtract it for comparison

        self.thump_pub = rospy.Publisher('thumps', Bool, queue_size=10)
        self.rate = rospy.Rate(Player.NODE_RATE) # 10 Hz

        if 'playback' in mode or 'off' in mode:
            self.mode=Player.OFF
            rospy.loginfo("Playing form file")
            beatfile=self.loadfile()
            self.beats=[float(tstamp)
 for tstamp in beatfile.readlines()]
            # for multicloumn
            # csv.reader(beats)
        else:
            self.mode=Player.LIVE
            rospy.loginfo("Player is live")
            self.beat_sub = rospy.Subscriber('beats', Beat, self.cb)
            #self.run=self.live


    def beat_cb(self,data):
        #playsound(self.note) # this has dep issues
        t_stmp=data.header.stamp.to_sec() #for now, let's find a sound module.
        self.beats.append(t_stmp)

    def model_cb(self,data):
        #playsound(self.note) # this has dep issues
        t_stmp=data.header.stamp.to_sec() #for now, let's find a sound module.
        self.model.update(t_stmp)

        pred=self.model.predict(1)#self.ahead

        rospy.logdebug("--------------------")
        rospy.logdebug("rcv.:   pred: ")
        rospy.logdebug(t_stmp)
        rospy.logdebug( pred[0])

    def play(self):
        #print('beep', t_stmp-self.beats[-1])
        #sys.stdout.write("\a")
        print('beep')


    def loadfile(self):
        try:
            path=input('Beat file:')


        except SyntaxError:
            path = 'txt/test.txt'
        if not path:
            path='txt/test.txt'
        return open(path, 'rU')

    def run_observed(self):

        T=1/Player.NODE_RATE #1/f, Period
        i=0
        print('T',T)

        # Offline assumes timer starts from 0
        # Live uses the timer marks coming from ros
        mark = (rospy.Time.now().to_sec() if not self.mode else 0)
        while not rospy.is_shutdown():
            if i < len(self.beats):
                elapsed=rospy.Time.now().to_sec() - mark
                #print('e',elapsed)
                #print(self.beats[i])
                if abs(elapsed-self.beats[i]) < T: #if we are in the correct t with a resolution of 1/rate
                    #self.play()
                    self.thump_pub.publish(True)
                    print(elapsed, elapsed-self.beats[i])
                    i+=1
                elif elapsed-self.beats[i] > T: #if running behind
                    i+=1

            self.rate.sleep()
    def run_predicted(self):
        
        T=1.0/Player.NODE_RATE #1/f, Period
        #rhthym_model=Model()
        print('T',T)
        # Offline assumes timer starts from 0
        # Live uses the timer marks coming from ros
        mark = (rospy.Time.now().to_sec() if not self.mode else 0)

        while not rospy.is_shutdown():
            if self.model.idx < len(self.model.predictions):
                diff=rospy.Time.now().to_sec() - mark -self.model.predictions[self.model.idx] + self.lag_adjustment
                #print(diff)
                #print('p:', self.model.predictions[i], 't:' , elapsed)
                if abs(diff) < T: #if we are in the correct t with a resolution of 1/rate
                    #self.play()
                    # - self.lag_adjustment !
                    self.thump_pub.publish(True)
                    print(60//self.model.m_n, " bpm" )
                    #rospy.logdebug("Fired with: ", diff, " s difference")
                    self.model.idx+=1
                elif diff > T: #if running behind
                    self.model.idx+=1

if __name__ == '__main__':
    try:
        if len(sys.argv) > 3 and sys.argv[3]:
            lvl = rospy.DEBUG
        else: lvl = rospy.INFO

        if len(sys.argv)>2:
            mode = sys.argv[1]
            pred = sys.argv[2]
        elif len(sys.argv)>1:
            mode = sys.argv[1]
            pred = 0
        else:
            mode,pred = "off", 0
        player = Player(mode, pred, lvl)
        player.run()
    except rospy.ROSInterruptException: pass
else:
    mode = rospy.get_param('~player_mode', 'live')
    player = Player(mode)
    player.run()
