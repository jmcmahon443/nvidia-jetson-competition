#! /usr/bin/env python
import pyaudio
import wave, time
import numpy as np
import aubio


CHUNK = 512
FORMAT = pyaudio.paFloat32
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

frames = []
# Pitch
tolerance = 0.8
downsample = 1
win_s = 1024 // downsample # fft size
hop_s = 512  // downsample # hop size
# pitch_o = pitch("yin", win_s, hop_s, RATE)
# pitch_o.set_unit("midi")
# pitch_o.set_tolerance(tolerance)

a_tempo = aubio.tempo("default", win_s, hop_s, RATE)

def pyaudio_callback(_in_data, _frame_count, _time_info, _status):
    audio_data = np.fromstring(_in_data, dtype=np.float32)

    is_beat = a_tempo(audio_data)
    if is_beat:
        #samples += click
        print('tick') # avoid print in audio callback
    #audiobuf = samples.tobytes()
    return (audio_data, pyaudio.paContinue)

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,
                stream_callback=pyaudio_callback)

print("* recording")

while stream.is_active():
    # buffer = stream.read(CHUNK)
    # frames.append(buffer)
    #
    # signal = np.fromstring(buffer, dtype=np.float32)
    #
    # pitch = pitch_o(signal)[0]
    # confidence = pitch_o.get_confidence()
    #
    # print('tick')
    time.sleep(0.1)


# pyaudio callback





print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()
