#!/bin/bash

# Get root permissions
# sudo pwd > /dev/null

# # Using pm
# sleep 1 && sudo pm-suspend &
# # In Gnome 3.28, screensaver is no longer built in
# # gnome-screensaver-command --lock
# dbus-send --type=method_call --dest=org.gnome.ScreenSaver /org/gnome/ScreenSaver org.gnome.ScreenSaver.Lock

# New method using systemd
systemctl -i suspend
# Shouldn't need to run lock command as machine should lock itself on suspend
