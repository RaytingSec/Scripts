#!/bin/bash
# Backup of user files for specified program
# Requires sudo to copy/delete program files and backups

# Standard static variables
PROGRAM=fail2ban
DATE=$(date +"%Y.%m.%d")
DIR=~/backup/$PROGRAM/$DATE/

# Ensure dir exists
# main backup dir
if [ ! -d ~/backup/ ];
then
   mkdir ~/backup/
fi
# program dir
if [ ! -d ~/backup/$PROGRAM/ ]
then
   mkdir ~/backup/$PROGRAM/
fi
# final dest dir
if [ ! -d "$DIR" ];
then
   mkdir $DIR
else
   sudo -s rm -r $DIR
   echo -e "Deleted existing dir"
fi

# Backup files
sudo -s cp -a /etc/$PROGRAM/ $DIR

# Compress to tarball
cd ~/backup/$PROGRAM/
sudo -s tar -cpzf ~/backup/$PROGRAM/$DATE.tar.gz $DATE
sudo -s rm -r $DIR

# Done
echo -e "Backed up to: $DIR"