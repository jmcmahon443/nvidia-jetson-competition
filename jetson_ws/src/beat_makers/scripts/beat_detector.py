#!/usr/bin/env python

import time, sys
import aubio, pyaudio
import rospy
import numpy as np
from beat_msgs.msg import Beat


class Player(object):

	source=[]
	rate=10
	def __init__(self):
		#ros
		rospy.init_node('beat_detector_node', anonymous=True)
		self.mode = rospy.get_param('~source', 'live')
		self.r = rospy.Rate(self.rate) # 10 Hz
		self.beat_pub = rospy.Publisher('beats', Beat, queue_size=10)

	def audio_init(self, filename, samplerate, win_s, hop_s):
		# create aubio source
		self.source = aubio.source(filename, samplerate, hop_s)
		samplerate = self.source.samplerate

		# create aubio tempo detection
		self.a_tempo = aubio.tempo("default", win_s, hop_s, samplerate)

		# create a simple click sound
		self.click = 0.7 * np.sin(2. * np.pi * np.arange(hop_s) / hop_s * samplerate / 3000.)

		self.audio = pyaudio.PyAudio()
		self.audio_format = pyaudio.paFloat32
		self.fpb = hop_s #frames_per_buffer

		n_channels = 1
		self.stream = self.audio.open(format=self.audio_format, channels=n_channels, rate=samplerate,
		        output=True, frames_per_buffer=self.fpb,
		        stream_callback=self.pyaudio_callback)

	def run(self):
		self.stream.start_stream()
		while not rospy.is_shutdown() and self.stream.is_active():
			self.r.sleep()
	def pub(self):
		a_beat=Beat()
		a_beat.beat=True # is assigning a member field and just updating stamp faster?
		self.beat_pub.publish(a_beat)

	# TODO: work on the audio input from mic

	def pyaudio_callback(self, _in_data, _frame_count, _time_info, _status):
	    samples, read = self.source()
	    is_beat = self.a_tempo(samples)
	    if is_beat:
	        samples += self.click
	        self.pub() # avoid print in audio callback
	    audiobuf = samples.tobytes()
	    if read < self.fpb: #also hopsize, hop_s
	        return (audiobuf, pyaudio.paComplete)
	    return (audiobuf, pyaudio.paContinue)


def parse():
	if len(sys.argv) < 2:
	    print("Usage: %s <filename> [samplerate]" % sys.argv[0])
	    sys.exit(1)

	filename = sys.argv[1]

	samplerate = 0
	if len( sys.argv ) > 2: samplerate = int(sys.argv[2])
	return filename, samplerate


if __name__ == '__main__':
    try:
		filename,sr=parse()
		win_s = 1024                # fft size
		hop_s = win_s // 2

		player = Player()
		player.audio_init(filename, sr, win_s, hop_s)
		player.run()

    except rospy.ROSInterruptException: pass
