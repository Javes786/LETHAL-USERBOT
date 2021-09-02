#!/bin/bash
clear
echo "
 _       _____   ____   _   _ 
| |     |_   _| / __ \ | \ | |
| |       | |  | |  | ||  \| |
| |       | |  | |  | || . ` |
| |____  _| |_ | |__| || |\  |
|______||_____| \____/ |_| \_|
                              
                              

"
echo Starting dependency installation in 5 seconds...
sleep 5
apt-get update
apt-get upgrade -y
pkg upgrade -y
pkg install python wget -y
wget https://raw.githubusercontent.com/Javes786/Lethal/master/Lethal-setup.py
pip install telethon
python Lethal-setup.py
