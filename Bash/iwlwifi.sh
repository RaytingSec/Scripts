#!/bin/bash

sudo modprobe -r iwlwifi
echo down
sleep 1
sudo modprobe iwlwifi
echo up
