# nvidia-jetson-competition
This is the software for the AI Bass Drum Pedal entry to the Nvidia Jetson embedded AI competition. Below is the basic software stack diagram.

![AI Bass Drum Pedal Software Diagram](diagram.png?raw=true "Diagram")

## Workstation installation
Make sure Python is installed.

```which python```

Clone this repository.

```git clone https://github.com/jmcmahon443/nvidia-jetson-competition.git```

Install `midiutil` and `madmom`.

```sudo pip install midiutil madmom```

## Jetson setup and installation
1. Plug-in power, HDMI monitor, mouse and keyboard. Hit the power button.
2. Follow Nvidia's installation steps shown at boot and reboot to Ubuntu desktop.
3. Connect to Wi-Fi (Nvidia Jetson TK1 requires a Wi-Fi module).
4. `sudo apt-get install vim`
5. `INSTALL PIP`
6. Follow the rest of the steps above to install the software.
7. `EDIT DEFAULT STARTUP TO GO TO COMMAND LINE, USE STARTX FOR DESKTOP`
8. `SET UP SSH`
