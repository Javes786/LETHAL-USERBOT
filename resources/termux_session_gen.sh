#!/bin/bash
clear
echo "

╔╗──╔═══╦════╦╗─╔╦═══╦╗
║║──║╔══╣╔╗╔╗║║─║║╔═╗║║
║║──║╚══╬╝║║╚╣╚═╝║║─║║║
║║─╔╣╔══╝─║║─║╔═╗║╚═╝║║─╔╗
║╚═╝║╚══╗─║║─║║─║║╔═╗║╚═╝║
╚═══╩═══╝─╚╝─╚╝─╚╩╝─╚╩═══╝

"
echo Starting dependency installation in 5 seconds...
sleep 5
apt-get update
apt-get upgrade -y
pkg upgrade -y
pkg install python wget -y
wget https://raw.githubusercontent.com/Javes786/LETHAL-USERBOT/main/Lethal-setup.py
pip install telethon
python Lethal-setup.py
