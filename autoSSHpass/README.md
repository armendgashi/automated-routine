# SSHPASS automated

Automate the noninteractive ssh password provider sshpass.

## Requirements

```
$ sudo apt-get install sshpass
$ pip3 install colorama
```

## Usage

```
$ chmod a+x sshpass.py
$ ./sshpass.py username password ip
```

Or copy this script as a binary.

```
$ cp sshpass.py /usr/bin/autosshpass
$ autosshpass username password ip
```
