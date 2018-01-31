#!/usr/bin/env python


import time
import rospy
from beat_msgs.msg import Beat


class Player(object):

	source=[]
	rate=10
	def __init__(self):
		
		rospy.init_node('beat_detector_node', anonymous=True)
		self.mode = rospy.get_param('~source', 'live')
		
		self.r = rospy.Rate(self.rate) # 10 Hz
		
		if self.mode is not 'playback':  
			self.beat_pub= rospy.Subscriber('beats', Beat, queue_size)
	
	
	def publish(self):
		raise NotImplemented
	
	
	def detect(self):
		raise NotImplemented
	
	
	# maybe change tihs to hooks for the same fcn.
	def runrecord(self):
		#playsound(self.note) # this has dep issues
		print('beep') #for now, let's find a sound module. 
	
		
	def runlive(self):
		
		while not rospy.is_shutdown():
	 		beat=self.detect()
			self.r.sleep()	

if __name__ == '__main__':
    try:
        player = Player()
        player.run()
    except rospy.ROSInterruptException: pass

