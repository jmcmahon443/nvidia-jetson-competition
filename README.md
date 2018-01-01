# nvidia-jetson-competition
This is the software for the AI Bass Drum Pedal entry to the Nvidia Jetson embedded AI competition. Below is the basic software stack diagram.

![AI Bass Drum Pedal Software Diagram](diagram.png?raw=true "Diagram")

## Workstation installation
1. Make sure Python is installed: `which python`.
2. Install and update `vim`: `sudo apt-get install vim`.
3. Install `midiutil` and `madmom`: `sudo pip install midiutil madmom`.

## Jetson setup and installation
1. Plug-in power, HDMI monitor, mouse and keyboard into Jetson. Hit the power button.
2. Follow Nvidia's installation steps shown at boot and reboot to Ubuntu desktop.
3. Connect to Wi-Fi (Sarmad's TK1 requires a Wi-Fi module and driver), or ethernet to router.
4. Install and update `vim`: `sudo apt-get install vim`.
5. `TODO: INSTALL PIP`.
6. Follow the steps above in "Workstation installation" to install the software.
7. `TODO: EDIT DEFAULT STARTUP TO GO TO COMMAND LINE, USE STARTX FOR DESKTOP`.

## `ssh` setup
1. Once Wi-Fi is setup on the Jetson, open a Terminal and type `ifconfig`.
2. Look for the local IP address next to `wlan0`, for example: `10.0.1.23`. If you are plugged in directly check `eth0`.
3. On your other workstation, type ping `10.0.1.23`, or whatever the IP adress you found earlier was.
4. On your workstation, add the IP to your list of known hosts by typing `sudo vim /etc/hosts` and adding the following line `jetson 10.0.1.23`. This will replace the name "jetson" with the IP address, so you do not have to memorize it.
5. Type `ifconfig` on your workstation and again note the IP address next to `wlan0`, for example: `10.0.1.8`.
6. Now back on the Jetson, add `sudo` access to the workstation, which will allow it to run `sudo` commands on the Jetson, remotely.
7. `TODO`.
8. `TODO`.
9. Unplug the monitor, mouse and keyboard and restart the Jetson.
10. `ssh` into the Jetson from your workstation: `ssh ubuntu@jetson`. You should not need to enter any password now, and can run `sudo`: `sudo su`.

## `git` setup
1. On both the workstation and the Jetson, clone this repository to your `~/Documents/` directory: `cd ~/Documents/; git clone https://github.com/jmcmahon443/nvidia-jetson-competition.git`.
2. Go into the directory and run `python test_install.py` to test the installation.
3. Just push any changes directly to `master` branch: `git add -A`
4. `git commit -m "YOUR_COMMIT_MESSAGE"`
5. `git push`

## Microphone
1. Plug in a microphone and run `python test_microphone.py` to test your microphone.
2. Record something: `python record.py YOUR_FILE_NAME`. It will automatically get saved as a .wav file.
3. Play it: `python play.py YOUR_FILE_NAME.wav`. It only accepts .wav files.
4. `TODO`.
