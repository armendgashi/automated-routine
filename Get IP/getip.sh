#!/usr/bin/bash

interface_status=$(cat /sys/class/net/$1/operstate)
if echo $interface_status | grep -q "down"; then
	echo -e "$1 is \e[31mDOWN\e[0m"
elif echo $interface_status | grep -q "up" || echo $interface_status | grep -q "unknown"; then
	vari=$(ifconfig $1 | grep inet | head -n 1 | cut -d ' ' -f 10)
	echo $vari | xclip -selection c
	echo -e "\e[32m$vari"
else
	echo -e "USAGE: \e[91m./wlan0.sh interface"
fi
