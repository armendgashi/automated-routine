#!/usr/bin/python3

import sys
import os
from colorama import Fore, Back, Style

username = sys.argv[1]
password = sys.argv[2]
ip = sys.argv[3]

while True:
    banner = '╭─[{}{}@{}{}]\n'.format(Fore.GREEN,username,ip,Fore.WHITE)
    shell = input('{}╰─>'.format(banner))
    if shell == "exit":
        break
    else:
        os.system("sshpass -p {} ssh {}@{} {}".format(password, username, ip, shell))
