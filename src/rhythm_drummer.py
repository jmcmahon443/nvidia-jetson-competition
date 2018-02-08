import rospy, time, sys

class Rhythm(object): #this is our predicted model
	def __init__(self, tempo=120,offset=0,pattern=[1, 0, 1, 0]):
	self.tempo= # bpm
	self.offset = 0
	self.pattern=[]
	self.meter=1 #or make a interval(Enum) to hold values 1/2,!/4 etc.
	self.interval=self.calc_interval()

	def calc.interval(self):
		self.interval = 60/tempo*duration

	def make_timekeys(self,n):
		# add mark for the current time
		#intervals= + offset #(s)
		pass


# Option 2:
#another way to approach this to have multiple f(x)={0:1} where f(x) is a signal function fith freq F and and offset of t


class RecurringBeat():
	def __init__(self,interval, offset=0): #msec
		rospy.sleep(Duration(0,offset))
		self.interval=interval
		self.stick=rospy.Timer(rospy.Duration(2), self.hit)
	# Potentially multithread this and add sleeps for offset adjustments.
	# altough, rospy is intrinsicly multithreaded, so this can be fine by itself
	# I would say syncing it with the global time would be smarter

	# Here is a nice way to keep track of things
	'''
	rospy.TimerEvent

		last_expected
			In a perfect world, this is when the previous callback should have happened.
		last_real
			This is when the last callback actually happened.
		current_expected
			In a perfect world, this is when the current callback should have been called.
		current_real
			When the current callback is actually being called (rospy.Time.now() as of immediately before calling the callback.)
		last_duration
			Contains the duration of the last callback (end time minus start time) in seconds. Note that this is always in wall-clock time.
		'''
	def hit(self): #callback, I am being fancy with names
		print("DUM")

	def correct(self,t):
		if t<0:
			rospy.sleep(Duration(0,abs(t)+interval)
		elif t is 0:
			pass
		else:
			rospy.sleep(Duration(0,t))


class Drummer(object):
	def __init__(self, mode):
		model=Rythm()

	def run():
		rospy.init_node("drummer",level=rospy.DEBUG, Anonymous=true) #is a ROS node or anythin that can sleep, or raise time events.




def main():
	drm=Drummer()
	drummer.start()

if __name__=='__main__':
	main()
	sys.exit()
else
	print("Drummer is imported")
