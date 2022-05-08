#!/bin/bash
# gui app deps installer 
pkgs="tk" 
pip_pysimplegui=$(pip install pysimplegui)
welcome="Welcome to Lain's Friendly Helper Station installer!"
installing="Installing the needed packages, hold tight..."
all_done="Packages installed. Exiting." 
notif_title="Lain's Friendly Helper Station Installer"
notif_content="Installation finished."
updating_sys="Updating your system first..."
function update {
    sudo pacman -Syu
}
########################
echo "$welcome"
sleep 1
echo "$updating_sys"
update
echo "$installing"
sleep 1
echo "Installing PySimpleGUI from pip..." 
$pip_pysimplegui
echo "Installing tk..."
sleep 1
sudo pacman -S $pkgs
echo "$all_done"
sleep 1
notify-send $notif_title $notif_content
exit