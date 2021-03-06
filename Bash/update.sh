#!/bin/bash
# Simple script to update packages on machine

if [[ "$1" == "" ]]; then # Update repos
    sudo apt update
    apt list --upgradable
elif [[ "$1" == "-l" ]]; then
    apt list --upgradable
    # alert
elif [[ "$1" == "--upgrade" ]] || [[ "$1" == "-u" ]] ; then # Upgrade packages
    sudo apt upgrade -y
    sudo apt autoremove -y
    # alert
elif [[ "$1" == '--help' ]]; then # help text
    echo "Sends update and upgrade commands to apt"
    echo "Options:"
    echo "    (blank)   ask and output for upgrades only"
    echo ""
    echo "All options except silent will print apt update errors"
else
    echo "option '$1' not recognized."
    echo "'--help' gives usage information."
fi

