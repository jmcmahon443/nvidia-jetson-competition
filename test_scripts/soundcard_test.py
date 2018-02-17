#if you have pulseudio 

import soundcard as sc

speakers = sc.all_speakers()
default_speaker = sc.default_speaker()
mics = sc.all_microphones()
default_mic = sc.default_microphone()
# search by substring:
one_speaker = sc.get_speaker('Scarlett')
one_mic = sc.get_microphone('Scarlett')
# fuzzy-search:
one_speker = sc.get_speaker('FS2i2')
one_mic = sc.get_microphone('FS2i2')
print(default_speaker)
print(default_mic)

# record and play back one second of audio:
data = default_mic.record(samplerate=44100, numframes=44100)
default_speaker.play(data/numpy.max(data), samplerate=44100)

# alternatively, get a `recorder` and `player` object and play or record continuously:
with default_mic.recorder(samplerate=44100) as mic, default_speaker.player(samplerate=44100) as sp:
    for _ in range(100):
        data = mic.record(numframes=1024)
        sp.play(data)
