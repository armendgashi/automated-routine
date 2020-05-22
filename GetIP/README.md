# GETIP

Shell script that prints out only the IP of your chosen Network Interface and copies it on your clipboard.

## Requirements

```
Make sure the following binaries are instelled on your system:
grep (sudo apt-get install grep)
xclip (sudo apt-get install grep)
```

## Usage

```
chmod a+x getip.sh
./getip.sh interface
```

## Example

```
./getip.sh wlan0

OR you can use it as a binary

cp getip.sh /usr/bin/getip
getip wlan0
```
