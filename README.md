# Automated Routine

Shell scripts to simplify linux processes.

## Installation

```
git clone https://github.com/armendgashi/automated-routine
```

## Usage

# GETIP

### Requirements

Make sure grep and xclip are instelled on your system:

```
$ sudo apt-get install grep
$ sudo apt-get install xclip
```

Shell script that prints out only the IP of your chosen Network Interface and copies it on your clipboard.

```
$ chmod a+x getip.sh
$ ./getip.sh interface
```

### Example

```
$ ./getip.sh wlan0
```

Or you can use it as a binary.

```
$ cp getip.sh /usr/bin/getip
$ getip wlan0
```

# Base64 Encoding/Decoding

Useful shell scripts for fast base64 encoding and decoding.

### Usage

```
$ chmod a+x base64_encode.sh
$ chmod a+x base64_decode.sh

$ ./base64_encode Text to encode
$ ./base64_decode Text to decode
```

### Example

```
$ ./base64_encode testing
$ ./base64_decode dGVzdGluZwo=
```

Or you can use them as a binary.

```
$ cp base64_encode /usr/bin/b64enc
$ cp base64_decode /usr/bin/b64dec

$ b64enc test
$ b64dec dGVzdGluZwo=
```

# SSHPASS automated

Automate the noninteractive ssh password provider sshpass.

### Requirements

```
sudo apt-get install sshpass
$ pip3 install colorama
```

### Usage

```
$ chmod a+x sshpass.py
$ ./sshpass.py username password ip
```

Or copy this script as a binary.

```
$ cp sshpass.py /usr/bin/autosshpass
$ autosshpass username password ip
```



![gif](https://user-images.githubusercontent.com/62258986/82859731-d122bb80-9f17-11ea-9948-6fd6c7ed9bf8.gif)
