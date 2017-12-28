# nvidia-jetson-competition
This is the software for the AI Bass Drum Pedal entry to the Nvidia Jetson embedded AI competition. Below is the basic software stack diagram.

![AI Bass Drum Pedal Software Diagram](diagram.png?raw=true "Diagram")

## Workstation installation
1. Make sure Python is installed: `which python`.
2. Install `midiutil` and `madmom`: `sudo pip install midiutil madmom`.
3. Clone this repository: `git clone https://github.com/jmcmahon443/nvidia-jetson-competition.git`.

## Jetson setup and installation
1. Plug-in power, HDMI monitor, mouse and keyboard into Jetson. Hit the power button.
2. Follow Nvidia's installation steps shown at boot and reboot to Ubuntu desktop.
3. Connect to Wi-Fi (Sarmad's TK1 requires a Wi-Fi module and driver).
4. Install and update `vim`: `sudo apt-get install vim`.
5. `INSTALL PIP`.
6. Follow the steps above in "Workstation installation" to install the software.
7. `EDIT DEFAULT STARTUP TO GO TO COMMAND LINE, USE STARTX FOR DESKTOP`.
8. `SET UP SSH`.
9. Unplug the monitor, mouse and keyboard and restart the Jetson.
10. `ssh` into the Jetson from your workstation: `SSH`.
