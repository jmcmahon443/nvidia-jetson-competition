#!/usr/bin/env python

import time, sys
import aubio, pyaudio
import rospy
import numpy as np
from beat_msgs.msg import Beat

RATE = 44100


class BeatMaker(object):
    LIVE=1
    OFFLINE=0

    source=[]
    rate=10
    def __init__(self):
        #ros
        rospy.init_node('beat_detector_node', anonymous=True)
        self.mode = rospy.get_param('~source', 'live')
        self.r = rospy.Rate(self.rate) # 10 Hz
        self.beat_pub = rospy.Publisher('beats', Beat, queue_size=10)

    def audio_init(self, filename, samplerate, win_s, hop_s):
        #pyaudio init.
        self.audio = pyaudio.PyAudio()
        self.audio_format = pyaudio.paFloat32
        self.fpb = hop_s
        n_channels = 1

        # initialize ros beat_msgs    self.msg=Beat()
        self.msg=Beat()
        self.msg.beat=True

        # select aubio source
        if (filename == "live"): # or source
            print("Tapping to the live input")
            self.mode=BeatMaker.LIVE
            samplerate=RATE
            self.btempo = aubio.tempo("default", win_s, hop_s, samplerate)

            self.stream = self.audio.open(format=self.audio_format, channels=n_channels, rate=samplerate,
                    input=True, frames_per_buffer=self.fpb,
                    stream_callback=self.mic_callback)

        else:
            print("Tapping to the audio file")
            self.mode=BeatMaker.OFFLINE
            self.source = aubio.source(filename, samplerate, hop_s)
            samplerate = self.source.samplerate
            self.btempo = aubio.tempo("default", win_s, hop_s, samplerate)

            self.stream =  self.audio.open(format=self.audio_format, channels=n_channels, rate=samplerate,
                        output=True, frames_per_buffer=self.fpb,
                        stream_callback=self.file_callback)
            self.click = 0.7 * np.sin(2. * np.pi * np.arange(hop_s) / hop_s * samplerate / 3000.)
        # create aubio tempo detection

        # create a simple click sound


#frames_per_buffer




    def run(self):
        self.stream.start_stream()
        while not rospy.is_shutdown() and self.stream.is_active():
            self.r.sleep()

    def pub(self):
         # is assigning a member field and just updating stamp faster?
        self.msg.header.stamp=rospy.Time.now()
        self.beat_pub.publish(self.msg)


    def file_callback(self, _in_data, _frame_count, _time_info, _status):
        samples, read = self.source()
        #print("s ",len(samples)) # len =512, floats
        #print("read ",read) # same with hopsize
        is_beat = self.btempo(samples)
        if is_beat:
            samples += self.click
            self.pub()
            #print('tick') # for debugging, don'T pring in cb

        audiobuf = samples.tobytes()
        if read < hop_s:
            return (audiobuf, pyaudio.paComplete)
        return (audiobuf, pyaudio.paContinue)


    def mic_callback(self, _in_data, _frame_count, _time_info, _status):
        audio_data = np.fromstring(_in_data, dtype=np.float32)
        is_beat = self.btempo(audio_data)
        if is_beat:
            #samples += click
            self.pub() # avoid print in audio callback
        #audiobuf = samples.tobytes()
        return (audio_data, pyaudio.paContinue)


def parse():

    if len(sys.argv) < 2:
      return "live", 0

    filename = sys.argv[1]
    samplerate = 0

    if len( sys.argv ) > 2: samplerate = int(sys.argv[2])
    return filename, samplerate


if __name__ == '__main__':
    try:
        filename,sr=parse()
        win_s = 1024                # fft size
        hop_s = win_s // 2

        bmk = BeatMaker()
        bmk.audio_init(filename, sr, win_s, hop_s)
        bmk.run()

    except rospy.ROSInterruptException: pass

# def record_sink(sink_path):
#     """Record an audio file using pysoundcard."""
#
#     from aubio import sink
#     from pysoundcard import Stream
#
#     hop_size = 256
#     duration = 5 # in seconds
#     s = Stream(blocksize = hop_size, channels = 1)
#     g = sink(sink_path, samplerate = int(s.samplerate))
#
#     s.start()
#     total_frames = 0
#     try:
#         while total_frames < duration * s.samplerate:
#             vec = s.read(hop_size)
#             # mix down to mono
#             mono_vec = vec.sum(-1) / float(s.channels[0])
#             g(mono_vec, hop_size)
#             total_frames += hop_size
#     except KeyboardInterrupt:
#         duration = total_frames / float(s.samplerate)
#         print("stopped after %.2f seconds" % duration)
#     s.stop()
#
# if __name__ == '__main__':
#     import sys
#     record_sink(sys.argv[1])
