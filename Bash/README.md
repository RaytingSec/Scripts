Bash
============

DESCRIPTION

Bash scripts intended to run on Debian. They were specifically written for my machines, so run a script only if the code has been reviewed and you know it's not going to cause trouble. A varying degree of manual editing is also needed to get certain scripts these working, i.e. server URLs.

SCRIPTS

update:  
Simple script that automates the apt-get update and upgrade command. Should be fully working "out of the box". It has three output levels:
Silent: no output except update errors and will not ask for upgrade permission
Verbose: outputs everything and asks for upgrade permission
Default: a mix of the two, outputs update errors and upgrade information but does NOT ask for upgrade permission
The script file also contains these details, but reading the few lines of script itself also tells you everything.

backup:  
Currently broken and will be fixed!
Takes predefined directories and files and compresses into a timestamped tar. It comes preloaded to backup most files for apache2, fail2ban, and openssh. 

firstboot:  
Automates setting up a new Linux machine. Check contents and know what you're doing before running this yourself. You will need to manually input version numbers into the script file. Not fully tested.

flood:
A fun script that covers the screen in 0s and 1s, inspired by the "matrix" effect.

raydartools:  
Common commands I use with my server. Not actually very practical, but saves some finger movement and memorization.

wgetter:  
A simple script that loops through designated URLs and applies the wget command to simultaneously download a series files in the background. For example, I used it to download a podcast archive. Coding on the user's part is REQURIED and will not work as-is.

More to come!

