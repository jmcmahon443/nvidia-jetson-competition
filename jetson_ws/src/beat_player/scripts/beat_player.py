#!/usr/bin/env python

from __future__ import division
import pygame.midi as midi
import pygame
import time
from playsound import playsound
import rospy
from beat_msgs.msg import Beat
import csv


class Player(object):
	kick='res/kick.mp3'
 
    

	rate=10
	def __init__(self):
		#pygame.init()
		#self.s = pygame.mixer.Sound(Player.kick)
    	
		rospy.init_node('beat_player_node', anonymous=True)
		self.mode = rospy.get_param('~player_mode', 'playback')
		
		self.r = rospy.Rate(self.rate) # 10 Hz
		
		if self.mode is not 'playback':  
			self.beat_sub = rospy.Subscriber('beats', Beat, self.play)
			self.run=self.live
		else:
			self.run=self.playback
			
			
	def play(self):
		#playsound(self.note) # this has dep issues
		print('beep') #for now, let's find a sound module. 
		#self.s.play()
	def loadfile(self):
		try:
			path=input('Beat file:')
			
		except SyntaxError:
			path = 'txt/test.txt'
		if not path:
			path='txt/test.txt'
		return open(path, 'rU')
		
	def playback(self):
		print("Playing form file")
	
		T=1/self.rate #1/f, Period
		beatfile=self.loadfile()
		beats=beatfile.readlines()
		# for multicloumn
		# csv.reader(beats)
		i=0
		mark = rospy.Time.now()			
		while i < len(beats):
			elapsed=rospy.Time.now() - mark
			if abs(elapsed.to_sec()-float(beats[i])) < T: #if we are in the correct t with a resolution of 1/rate	
				self.play()
				i+=1
							
	def live(self):
		print("Player is live")
		while not rospy.is_shutdown():
	 		
			self.r.sleep()	

if __name__ == '__main__':
    try:
        player = Player()
        player.run()
    except rospy.ROSInterruptException: pass



