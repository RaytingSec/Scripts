#!/bin/bash

# sudo pwd > /dev/null
sleep 1 && sudo pm-suspend &
gnome-screensaver-command --lock
