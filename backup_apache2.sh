#!/bin/bash
# Backup of user files for specified program
# Requires sudo to copy/delete program files and backups

# Standard static variables
PROGRAM=apache2
DATE=$(date +"%Y.%m.%d")
DIR_PGR=~/backup/$PROGRAM
DIR_TMP=~/backup/$PROGRAM/$DATE
TAR=$DATE.tar.gz
BACKUP=(
        /etc/$PROGRAM/
        /var/www/
       )
ARRAY_SIZE=${#BACKUP[@]}



# Ensure dir exists
# main backup dir
if [ ! -d ~/backup/ ];
then
   echo -e "WARNING! Main backup dir does not exist!"
   mkdir ~/backup/
fi
# program dir
if [ ! -d $DIR_PGR ]
then
   mkdir $DIR_PGR
fi
# dest dir
if [ ! -d "$DIR_TMP" ];
then
   mkdir $DIR_TMP
else
   sudo -E rm -r $DIR_TMP
   echo -e "Deleted existing dir"
fi

# Backup files
#sudo -E cp -a /etc/$PROGRAM/ $DIR
#sudo -E cp -a ~/.ssh $DIR
#sudo -E cp -a /etc/motd $DIR
#sudo -E cp -a /etc/issue $DIR
#sudo -E cp -a /etc/issue.net $DIR
let "i=0"
while [ $i -ne $ARRAY_SIZE ]; do
    sudo -E cp -a ${BACKUP[$i]} $DIR_TMP
    let "i++"
done

# Compress to tarball
cd $DIR_PGR
# if tarball exists
if [ -d "$TAR" ]
then
   rm $TAR
   echo -e "Deleted existing tar"
fi
# create tarball
sudo -E tar -cpzf $DIR_PGR/$TAR $DATE
sudo -E rm -r $DIR_TMP

# Done
echo -e "Backed up to: $DIR_PGR/$TAR"
