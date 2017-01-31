#!/bin/bash
# Configure a fresh Linux installation

# Packages
HOST=true
VM=true
DEV=true
SERVER=false
UNITY=false
XFCE=false
CIN=false

# Libraries

# Find data dir
DATA=/home/$USER/Data
if [ -d "/data" ]; then
    ln -s /data ~/Data
    echo "Using /data"
elif [ -d $DATA ]; then
    echo "Using ~/data"
else
    echo "No data directory found, exiting"
    exit 1
fi

# Drivers if necessary
bash ./drivers.sh

# Link to common dirs
bash ./directories.sh

# Configure things
bash ./configure.sh

# Install packages
bash ./packages.sh
