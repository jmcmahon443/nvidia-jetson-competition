#!/usr/bin/env python

from __future__ import division
import pygame.midi as midi
import pygame
import time
#from playsound import playsound
import rospy
from beat_msgs.msg import Beat
import csv





def predict(self, next_n):
	presum=0
	I=0
	e=0
	e_sum=0
	print(0, "	",beats[0], "  ", "-", "  ", "-")
	for i in range(1,len(beats)-1): #care elemnt number vs index
		I+=i
		presum+=normalized[i-1]
		next=(presum/I)*(i+1)+beats[0]
		adjusted_next=((presum-e_sum)/(I+e))*(i+1)
		e=adjusted_next-beats[i]
		e_sum+=e


class Player(object):
	KICK='res/kick.mp3'
	NODE_RATE=20

	def __init__(self):
		#pygame.init()
		#self.s = pygame.mixer.Sound(Player.kick)
		self.beats=[0]
		self.predicted=[] #add the actuator delay here, subtract it for comparison
		rospy.init_node('beat_player_node', anonymous=True)
		self.mode = rospy.get_param('~player_mode', 'live')

		self.rate = rospy.Rate(Player.NODE_RATE) # 10 Hz

		if self.mode is not 'playback':
			print("Player is live")
			self.beat_sub = rospy.Subscriber('beats', Beat, self.beat_cb)
			#self.run=self.live
		else:
			print("Playing form file")
			beatfile=self.loadfile()
			beats=[float(tstamp) for tstamp in beatfile.readlines()]

	def beat_cb(self,data):
		#playsound(self.note) # this has dep issues
		t_stmp=data.header.stamp.to_sec()
		print('beep', t_stmp-self.beats[-1] ) #for now, let's find a sound module.
		self.beats.append(t_stmp)
	def play(self):
		pass
		#self.s.play()
	def loadfile(self):
		try:
			path=input('Beat file:')

		except SyntaxError:
			path = 'txt/test.txt'
		if not path:
			path='txt/test.txt'
		return open(path, 'rU')

	def run(self):

		T=1/Player.NODE_RATE #1/f, Period
		i=0
		# for multicloumn
		# csv.reader(beats)

		while not rospy.is_shutdown():
			mark = rospy.Time.now()
			if i < len(self.beats):
				elapsed=rospy.Time.now() - mark
				if abs(elapsed.to_sec()-self.beats[i]) < T: #if we are in the correct t with a resolution of 1/rate
					self.play()
					i+=1
			else:
				pass
			self.rate.sleep()


if __name__ == '__main__':
    try:
        player = Player()
        player.run()
    except rospy.ROSInterruptException: pass
