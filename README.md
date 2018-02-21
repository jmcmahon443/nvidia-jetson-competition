# beats-by-jetson
This is the software for the AI Bass Drum Pedal "Beats by Jetson" entry to the 2018 NVIDIA Jetson Developer Competition.
cd into jetson_ws and catkin build. Source the workspace and then:
```
roscore
python beat_makers/beat_detector.py (or keyboard2beats.py for manual input)
python master_of_beats/beat_predictor.py live 1 
python beat_players/drummer/whiplash.py 1 1 
```
Or use the provided .launch files.
## Workstation installation
1. Make sure Python is installed: `which python`.
2. Install DPKG packages `sudo apt-get install vim ffmpeg python-portaudio aubio`.
  .Optionally you can get aubio from https://git.aubio.org/aubio/aubio/
  *Jack2d is recommended*
3. Install PIP packages: `sudo pip install cython numpy scipy midiutil madmom pyaudio pysoundcard aubio`.


## Jetson setup and installation
1. Plug-in power, HDMI monitor, mouse and keyboard into Jetson. Hit the power button.
2. Follow Nvidia's installation steps shown at boot and reboot to Ubuntu desktop.
3. Connect to Wi-Fi (Sarmad's TK1 requires a Wi-Fi module and driver), or ethernet to router.
4. Follow the directions for the stepper motor software, which is cloned at `output/nvidia-jetson-competition/output/Adafruit-Motor-HAT-Python-Library`: https://learn.adafruit.com/adafruit-dc-and-stepper-motor-hat-for-raspberry-pi/installing-software


## `git` setup
1. On both the workstation and the Jetson, clone this repository to your `~/Documents/` directory: `cd ~/Documents/; git clone https://github.com/jmcmahon443/nvidia-jetson-competition.git`.
2. Go into the directory and run `python test_install.py` to test the installation.
3. Just push any changes directly to `master` branch: `git add -A`
4. `git commit -m "YOUR_COMMIT_MESSAGE"`
5. `git push`
