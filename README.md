# Automated Routine

Shell scripts to simplify linux processes

## Installation

```
git clone https://github.com/armendgashi/automated-routine
```

## Usage

# GETIP

### Requirements

```
Make sure the following binaries are instelled on your system:

grep (sudo apt-get install grep)
xclip (sudo apt-get install xclip)
```

Shell script that prints out only the IP of your chosen Network Interface and copies it on your clipboard.

```
chmod a+x getip.sh
./getip.sh interface
```

### Example

```
./getip.sh wlan0

OR you can use it as a binary

cp getip.sh /usr/bin/getip
getip wlan0
```

# Base64 Encoding/Decoding

Useful shell scripts for fast base64 encoding and decoding.

### Usage

```
chmod a+x base64_encode.sh
chmod a+x base64_decode.sh

./base64_encode Text to encode
./base64_decode Text to decode
```

### Examples

```
./base64_encode testing
./base64_decode dGVzdGluZwo=

OR you can use them as a binary

cp base64_encode /usr/bin/b64enc
cp base64_decode /usr/bin/b64dec

b64enc test
b64dec dGVzdGluZwo=
```

# SSHPASS automated

Automate the noninteractive ssh password provider sshpass.

## Requirements

```
pip3 install colorama
```

## Usage

```
chmod a+x sshpass.py
./sshpass.py username password ip

OR copy this script as a binary
cp sshpass.py /usr/bin/autosshpass

autosshpass username password ip
```
