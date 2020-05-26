#!/usr/bin/python3

from optparse import OptionParser
import sys
import os
from colorama import Fore, Back, Style

def optParser():
    parser = OptionParser()
    parser.add_option("-u", "--username", dest="username", help="Target's Username")
    parser.add_option("-i", "--ip", dest="ip", help="Target's IP")
    parser.add_option("-p", "--password", dest="password", help="Target's Password")

    (options, args) = parser.parse_args()

    if not options.username or not options.ip or not options.password:
        print (parser.error("python3 sshpass.py --help"))
    else:
        return options

def main():
    options = optParser()
    while True:
        command = (input('[{}{}@{}{}]$ '.format(Fore.GREEN,options.username,options.ip,Fore.WHITE)))
        if command == "exit":
            break
        else:
            os.system("sshpass -p {} ssh {}@{} {}".format(options.password, options.username, options.ip, command))

if __name__ == "__main__":
    main()
