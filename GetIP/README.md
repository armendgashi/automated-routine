# GETIP

## Requirements

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

## Example

```
$ ./getip.sh wlan0
```

Or you can use it as a binary.

```
$ cp getip.sh /usr/bin/getip
$ getip wlan0
```
