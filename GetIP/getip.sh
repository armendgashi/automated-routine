#!/usr/bin/bash

interfaces_list=$(ls /sys/class/net)
interface_status=$(cat /sys/class/net/$1/operstate)
if echo $interface_status | grep -q "down"; then
        echo -e "$1 is \e[31mDOWN\e[0m"
elif echo $interface_status | grep -q "up" || echo $interface_status | grep -q "unknown"; then
        ip=$(ifconfig $1 | grep inet | head -n 1 | cut -d ' ' -f 10)
        echo $ip | xclip -selection c
        echo -e "\e[32m$ip"
else
        echo -e "\n\e[31mAvailable interfaces: \e[0m"
        echo $interfaces_list
        echo -e "\nUSAGE: \e[91m./wlan0.sh interface"
fi
