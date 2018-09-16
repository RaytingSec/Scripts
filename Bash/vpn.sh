#!/bin/bash

CONFIG=/etc/openvpn/ovpn_udp/us1448.nordvpn.com.udp.ovpn
USERPASS=/etc/openvpn/auth.txt
LOG=/etc/openvpn/$(date -Iseconds)_ovpn.log

helptext="Utilities for connecting to a vpn using OpenVPN
Options:
    (blank)   connect to vpn
    -c        cat current resolv.conf
    -d        overwrite entire resolv.conf with Google dns
    -k        kill the vpn
    -f        follow vpn log
"

set_dns () {
    # Google
    # printf 'nameserver 8.8.8.8\nnameserver 8.8.4.4\n' | sudo -E tee /etc/resolv.conf
    # OpenDNS
    # printf 'nameserver 208.67.222.222\nnameserver 208.67.220.220\n' | sudo -E tee /etc/resolv.conf
    printf 'nameserver 1.1.1.1\n' | sudo -E tee /etc/resolv.conf
}

vpn_connect () {
    sudo openvpn --config $CONFIG --auth-user-pass $USERPASS \
                 --verb 4 --log $LOG --daemon
    sudo gnome-terminal --command="tail -fn 50 $LOG"
}

# Default start vpn
if [[ "$1" == "" ]]; then
    vpn_connect

# prints resolv.conf contents
elif [[ "$1" == "-c" ]]; then
    cat /etc/resolv.conf

# config dns
elif [[ "$1" == "-d" ]]; then
    set_dns

# force kill
elif [[ "$1" == "-k" ]]; then
    sudo pkill -INT openvpn

# follow log
elif [[ "$1" == "-f" ]]; then
    sudo gnome-terminal --command="tail -fn 50 $LOG"

# help text
elif [[ "$1" == "--help" ]]; then # help text
    echo "$helptext"

# unknown
else
    echo "option '$1' not recognized."
    echo "'--help' gives usage information."

fi

