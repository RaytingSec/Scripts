#!/bin/bash

# Some getopts magic that creates repo and packages list

REPOS=()
PACKAGES=()
# General
REPOS+=(
    "ppa:webupd8team/sublime-text-3"
)
PACKAGES+=(
    "vim"
    "fortune"
    "cowsay"
    "fortunes"
    # "fortunes-debian-hints"
    # "fortunes-off"
    # "fortunes-spam"
    # "fortunes-ubuntu-server"
    "lolcat"
    "tmux"
    "htop"
    "atop"
    "tree"
    "finger"
    "whois"
    "traceroute"
    "nmap"
    # General network utilities    
    "hping3"
    "curl"
    "sshfs"
    "openvpn"
    "lynx-cur"
    "git"
    "fonts-hack-otf"
    "scanmem"
    # Administration things
    "libnotify-bin"
    "inotify-tools" # inotifywait
    "iptstate"
    # May be needed for adding repos
    # "python-software-properties"
    # "software-properties-common"
    "gpart"
    "gparted"
    "sublime-text-installer"
    "synaptic"
    "hexchat"
    # For fun
    "bsdgames"
    "bsdgames-nonfree"
)

# Host machine
if [ $HOST = true ]; then
    REPOS+=(
        "ppa:jtaylor/keepass"
        "ppa:maarten-baert/simplescreenrecorder"
    )
    PACKAGES+=(
        "cpufrequtils"
        "youtube-dl"
        "libav-tools"
        "vlc"
        "keepassx"
        # "xdotool"
        "steam"
        "simplescreenrecorder"
        "nautilus-dropbox"
        "audacity"
    )
# VM
elif [ $VM = true ]; then
    PACKAGES+=(
        "ssh"
        "open-vm-tools-desktop"
        "open-vm-tools-dkms"
    )
fi

# Development/Security
if [ $DEV = true ]; then
    REPOS+=(
        "ppa:webupd8team/java"
        "ppa:webupd8team/brackets"
        "ppa:gns3/ppa"
    )
    PACKAGES+=(
        # JDK
        "oracle-java8-installer"
        "oracle-java8-set-default"
        # Plugins and stuff
        "icedtea-plugin"
        "icedtea-8-plugin"
        # "flashplugin-installer"
        # Python
        "python3-pip"
        "python3-bs4"
        "python3-markdown"
        "python3-requests"
        "python3-crypto"
        "python3-numpy"
        "python3-mayplotlib"
        "python3-tk"
        # "python3-nacl"
        # "python-keyczar"
        "nodejs"
        "npm"
        "node-typescript"
        "brackets"
        "httpie"
        "sqlitebrowser"
        "gns3-gui"
        "gns3-iou"
        # Security
        "sox"
        "libsox-fmt-mp3"
        "nikto"
        "hydra"
        "sqlmap"
        "masscan"
        "zmap"
        "wireshark"
        "radare2"
    )
fi

# Server
if [ $SERVER = true ]; then
    REPO+=(
        "ppa:transmissionbt/ppa"
    )
    PACKAGES+=(
        "ssh"
        "mysql-server"
        "mysql-workbench"
        # Transmission stuff if building a seed box
        "transmission-cli"
        "transmission-daemon"
        "transmission-common"
    )
fi

# Unity
if [ $UNITY = true ]; then
    PACKAGES+=(
        "unity-tweak-tool"
        "gnome-color-chooser"
    )
# KDE
if [ $KDE = true ]; then
    REPOS+=(
        "ppa:kubuntu-ppa/backports"
    )
    PACKAGES+=(
        "kubuntu-desktop"
    )
# XFCE
elif [ $XFCE = true ]; then
    PACKAGES+=(
        "thunar-dropbox-plugin"
    )
# Cinnamon
elif [ $CIN = true ]; then
    REPOS+=(
        "ppa:tsvetko.tsvetkov/cinnamon"
    )
    PACKAGES+=(
        "cinnamon"
        "cinnamon-themes"
        "mint-backgrounds*"
        "nemo-dropbox"
        "mint-x-icons"
        "mint-themes"
        "cinnamon-session"
    )
fi

for R in "${REPOS[@]}"; do
    echo "sudo add-apt-repository -y "$R
done

SELECTED=""
for P in "${PACKAGES[@]}"; do
    SELECTED+=$P" "
done
echo "sudo apt install "$SELECTED


# Don't forget python packages

# Python development
sudo -H pip3 install --upgrade pip3
sudo -H pip3 install setuptools requests[security]
