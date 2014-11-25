#!/bin/bash
# Backup of user files for specified program
# Requires sudo to copy/delete program files and backups

# Standard static variables
PROGRAM=ssh
DATE=$(date +"%Y.%m.%d")
DIR=~/backup/$PROGRAM/$DATE/

# Ensure dir exists
# main backup dir
if [ ! -d ~/backup/ ];
then
   echo -e "WARNING! Main backup dir does not exist!"
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
   sudo -E rm -r $DIR
   echo -e "Deleted existing dir"
fi

# Backup files
sudo -E cp -a /etc/$PROGRAM/ $DIR
sudo -E cp -a ~/.ssh $DIR
sudo -E cp -a /etc/motd $DIR
sudo -E cp -a /etc/issue $DIR
sudo -E cp -a /etc/issue.net $DIR

# Compress to tarball
cd ~/backup/$PROGRAM/
# if tarball exists
if [ -d "$DATE.tar.gz" ]
then
   rm $DATE.tar.gz
fi
# create tarball
sudo -E tar -cpzf ~/backup/$PROGRAM/$DATE.tar.gz $DATE
sudo -E rm -r $DIR

# Done
echo -e "Backed up to: $DIR"
